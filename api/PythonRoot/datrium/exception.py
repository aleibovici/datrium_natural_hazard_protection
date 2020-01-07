##############################################################
# Copyright (c) 2012-2017 Datrium, Inc. All rights reserved. #
#                -- Datrium Confidential --                  #
##############################################################

"""
PB message classes are dynamically instantiated via reflection. This makes it
hard for them to be direct subclasses of Exception. To get around this, we
hacked the protoc compiler (python_generator.cc) to generate two classes for
each DaException. The first class ends with "Message" and is the PB message
class. The second class is the actual Exception. Each DaException* class derives
from DaException (defined here). This is so that:

1. DaExceptions can be raised naturally in Python server code.

2. The PyBridge server implementation can easily cast DaExceptions to
   DaExceptionBase(Message), which is the defined over-the-wire format for
   DaExceptions.

3. The PyBridge client implementation can easily create Python DaExceptions from
   DaErrs.

4. The pure Python server implementation can easily create Python DaExceptions
   from DaExceptionBase(Message) messages.

Here are some doctest examples.

# All of the Exceptions defined in Exception_pb2.py are sub-classes of
# DaException, which is why imports are done lazily.
>>> from IDL.Protos.Extensions.Exception_pb2 import *

# Can create and raise a DaException just as you would any other
# Exception. Message-specific attributes defined in Exception.proto should be
# specified as keywords, and are stored in attributes of the DaException.
>>> e = DaExceptionObjectNotFound('Container not found', notFoundId='0000000012345678')
>>> e.notFoundId
'0000000012345678'

# The error code is 1101. The error code chain lists all of its base codes and
# is for backward compatibility.
>>> e.ERROR_CODE
1101
>>> e.errorCodes
[1101, 1100, 1002]

# It is a real subclass.
>>> isinstance(e, DaExceptionNotFound)
True
>>> isinstance(e, DaExceptionUnchecked)
True
>>> isinstance(e, DaExceptionBase)
True
>>> isinstance(e, DaExceptionChecked)
False
>>> isinstance(e, DaExceptionLocalOnly)
False

# Can get the error message from either Exception.message or
# DaException.errorMsg (or if you are really perverse,
# DaException.base_message().errorMsg).
>>> e.message
'Container not found'
>>> e.errorMsg
'Container not found'
>>> e.base_message().errorMsg
u'Container not found'

# The pure Python RPC client uses create_exception_from_base_message() to
# convert over-the-wire DaExceptionBase to DaException.
>>> f = DaException.create_exception_from_base_message(e.base_message())
>>> e.base_message() == f.base_message()
True
>>> f.notFoundId
u'0000000012345678'

# The PyBridge RPC client uses create_exception() to convert DaErr to
# DaException to throw to Python.
>>> g = DaException.create_exception(e.ERROR_CODE, e.errorMsg, e.fileName, e.lineNum, \
                                     notFoundId=e.notFoundId)
>>> e.base_message() == g.base_message()
True
>>> g.notFoundId
'0000000012345678'
"""

from datrium.utils import kv_utils
from IDL.Protos.Extensions.KeyValueTypes_pb2 import KeyValue, TypedValue

class DaException(Exception):
    def __init__(self, errorMsg=None, fileName=None, lineNum=None, errorCodes=None, **kwargs):
        """
        Create a new instance of a DaException* subclass. The DaException class
        should not be instantiated directly!

        :param errorMsg: If not None, the error message text.
        :param fileName: If not None, the file where the error was generated.
        :param lineNum:  If not None, the line number in the file where the error was generated.
        :param kwargs:   Extended attributes.
        :returns:        New instance.
        """

        Exception.__init__(self, errorMsg)

        self.errorMsg = errorMsg
        self.fileName = fileName
        self.lineNum = lineNum
        self.errorCodes = errorCodes

        # Get fileName and lineNum from traceback, if not specified.
        if self.fileName is None and self.lineNum is None:
            import traceback
            self.fileName, self.lineNum, funcName, line = traceback.extract_stack()[-2]

        # Derive error codes of this class and all base classes.
        if self.errorCodes is None:
            self.errorCodes = []
            exception = self
            while exception.BASE_CLASS != None:
                assert exception.ERROR_CODE not in self.errorCodes
                self.errorCodes.append(exception.ERROR_CODE)
                exception = exception.BASE_CLASS

            # Sort them in reverse order by error code.
            self.errorCodes.sort(reverse=True)

        # Set additional attributes from kwargs.
        for key, val in kwargs.iteritems():
            if key in self.DESCRIPTOR.fields_by_name:
                setattr(self, key, val)

    @property
    def message(self):
        """
        Get the error message text.

        :returns: Current error message text.
        """

        return self.errorMsg

    def __repr__(self):
        """
        Get a best-effort representation of how the current DaException instance
        could be re-instantiated.

        :returns: Representation of the DaException instance.
        """

        # Basic arguments.
        args = map(repr, [self.errorMsg, self.fileName, self.lineNum, self.errorCodes])

        # Additional attributes.
        for key, field in self.DESCRIPTOR.fields_by_name.iteritems():
            val = getattr(self, key, None)
            if val is not None:
                args.append(key + "=" + repr(val))

        return type(self).__name__ + "(" + ", ".join(args) + ")"

    def __str__(self):
        """
        Get the string representation of the DaException.

        :returns: String representation of the PB message.
        """

        return repr(self) + "\n" + str(self.base_message())

    def base_message(self):
        """
        Encode the DaException to a DaExceptionBaseMessage and return it.

        :returns: DaExceptionBaseMessage.
        """

        from IDL.Protos.Extensions.Exception_pb2 import DaExceptionBaseMessage

        base_message = DaExceptionBaseMessage()

        assert self.errorCodes is not None
        base_message.errorCodes[:] = self.errorCodes

        if self.errorMsg is not None:
            base_message.errorMsg = self.errorMsg
        if self.fileName is not None:
            base_message.fileName = self.fileName
        if self.lineNum is not None:
            base_message.lineNum = self.lineNum

        # Set base_message.attributes from additional attributes.
        for key, field in self.DESCRIPTOR.fields_by_name.iteritems():
            if key not in ("errorMsg", "fileName", "lineNum", "errorCodes"):
                val = getattr(self, key, None)
                if val is not None:
                    attribute = base_message.attributes.add()
                    attribute.key = key
                    kv_utils.set_typed_val_from_val(attribute.val, val)

        return base_message

    @staticmethod
    def create_exception(error_code, errorMsg=None, fileName=None, lineNum=None, **kwargs):
        """
        Factory method. Given an error code, return an instance of the
        appropriate DaException subclass. Make sure to specify any required
        extended attributes in kwargs!

        :returns: New instance of the appropriate DaException subclass, or
                  DaExceptionBase if not found.
        """

        from IDL.Protos.Extensions.Exception_pb2 import EXCEPTIONS_BY_ERROR_CODE, DaExceptionBase

        if error_code in EXCEPTIONS_BY_ERROR_CODE:
            exception_class = EXCEPTIONS_BY_ERROR_CODE[error_code]
            # None means derive self.errorCodes[].
            errorCodes = None
        else:
            # Cannot find an appropriate class. Return DaExceptionBase.
            exception_class = DaExceptionBase
            errorCodes = [error_code]

        # We currently save the possibly bogus error code in self.errorCodes[]
        # for debugging. Maybe we should assert instead.

        return exception_class(errorMsg, fileName, lineNum, errorCodes, **kwargs)

    @staticmethod
    def create_exception_from_base_message(base_message, **kwargs):
        """
        Factory method. Given a DaExceptionBaseMessage, return an instance of
        the appropriate DaException subclass.

        :returns: New instance of the appropriate DaException subclass, or
                  DaExceptionBase if not found.
        """

        from IDL.Protos.Extensions.Exception_pb2 import EXCEPTIONS_BY_ERROR_CODE, DaExceptionBase

        for error_code in base_message.errorCodes:
            if error_code in EXCEPTIONS_BY_ERROR_CODE:
                exception_class = EXCEPTIONS_BY_ERROR_CODE[error_code]
                break
        else:
            # Cannot find an appropriate class. Return DaExceptionBase.
            exception_class = DaExceptionBase

        # Set additional attributes from base_message.attributes.
        # XXX (mhuang): What do we do if the base_message does not specify
        # required attributes?!
        attributes = dict((attribute.key, kv_utils.get_val_from_typed_val(attribute.val))
                          for attribute in base_message.attributes
                          if attribute.key not in ("errorMsg", "fileName", "lineNum", "errorCodes"))

        # kwargs will override any attributes from the base message.
        for k,v in kwargs.iteritems():
            attributes[k] = v

        # We currently save the possibly bogus error codes in self.errorCodes[]
        # for debugging. Maybe we should assert instead.

        return exception_class(base_message.errorMsg if base_message.HasField("errorMsg") else None,
                               base_message.fileName if base_message.HasField("fileName") else None,
                               base_message.lineNum if base_message.HasField("lineNum") else None,
                               base_message.errorCodes[:],
                               **attributes)

if __name__ == "__main__":
    # This runs the test examples above.
    import doctest
    doctest.testmod(verbose=True)
