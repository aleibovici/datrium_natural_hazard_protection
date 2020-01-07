#**************************************************************
#* Copyright (c) 2014-2018 Datrium, Inc. All rights reserved. *
#*                -- Datrium Confidential --                  *
#**************************************************************
from IDL.Protos.Extensions.KeyValueTypes_pb2 import TypedValue, KeyValue


def get_val_from_typed_val(tv):
    """
    Helper function to get the python values from a TypedValue.

    @param tv: Initialized TypedValue.
    @return: Python Value.
    """
    val = None
    if tv.type == TypedValue.Type.BOOL:
        val = tv.boolVal
    elif tv.type == TypedValue.Type.ENUM:
        val = tv.enumVal
    elif tv.type == TypedValue.Type.INT32:
        val = tv.int32Val
    elif tv.type == TypedValue.Type.INT64:
        val = tv.int64Val
    elif tv.type == TypedValue.Type.MSG:
        from type_map import type_map
        msg_name = tv.msgVal.msgType
        msg_instance = type_map[msg_name]()
        populate_msg_from_kv_list(msg_instance, tv.msgVal.keyVal)
        val = msg_instance
    elif tv.type == TypedValue.Type.STRING:
        # XXX (mhuang): Decode as UTF-8?
        val = tv.stringVal
    elif tv.type == TypedValue.Type.REPEATED_STRING:
        # XXX (mhuang): Decode as UTF-8?
        val = tv.repeatedStringVal
    else:
        assert False
    return val

def set_typed_val_from_val(tv, val):
    """
    Helper function to set a TypedValue from a Python value.

    @param tv: Uninitialized TypedValue.
    @param val: Python value.
    """
    if isinstance(val, bool):
        tv.type = TypedValue.Type.BOOL
        tv.boolVal = val
    elif isinstance(val, int):
        tv.type = TypedValue.Type.INT32
        tv.int32Val = val
    elif isinstance(val, long):
        tv.type = TypedValue.Type.INT64
        tv.int64Val = val
    elif isinstance(val, basestring):
        tv.type = TypedValue.Type.STRING
        # XXX (mhuang): Assume UTF-8 encoding.
        tv.stringVal = val.encode("utf-8")
    elif isinstance(val, list):
        assert all(isinstance(item, basestring) for item in val)
        tv.type = TypedValue.Type.REPEATED_STRING
        tv.repeatedStringVal[:] = [item.encode("utf-8") for item in val]
    else:
        # TODO (mhuang, ssen): Handle recursive marshaling of Message types.
        raise Exception("Cannot marshal %s!" % repr(val))

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

def make_key_value_from_dict(d):
    """
    Given a dictionary encoding a KeyValue object, construct and return
    a true KeyValue object.
    """
    kv = KeyValue()
    kv.key = d['key']
    faux_tv = AttrDict(d['val'])
    set_typed_val_from_val(kv.val, get_val_from_typed_val(faux_tv))
    return kv

def populate_msg_from_kv_list(msg, kv_list):
    """
    Given a key value list and message does a best effort to populate message properties
    from the individual key values.

    @param msg: The Message
    @param kv_list: The list of key values
    """
    for kv in kv_list:
        if hasattr(msg, kv.key):
            tv = kv.val
            val = get_val_from_typed_val(tv)
            setattr(msg, kv.key, val)

def get_value_with_key(kv_list, key):
    """
    Pick out the value for a given key.
    """
    for kv in kv_list:
        if isinstance(kv, dict):
            kv = make_key_value_from_dict(kv)
        if kv.key == key:
            return get_val_from_typed_val(kv.val)
    return None
