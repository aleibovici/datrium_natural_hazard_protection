# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: KeyValueTypes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from IDL.Protos.Extensions import CustomOptions_pb2 as IDL_dot_Protos_dot_Extensions_dot_CustomOptions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name='KeyValueTypes.proto',
    package='da.api',
    syntax='proto2',
    serialized_pb=_b('\n\x13KeyValueTypes.proto\x12\x06\x64\x61.api\x1a)IDL/Protos/Extensions/CustomOptions.proto\"\xa1\x01\n\x07\x45numVal\x12\x36\n\x08\x65numType\x18\x01 \x02(\tB\x1a\x92?\x17\x32\x15\x45numeration type nameR\x08\x65numType\x12;\n\tenumValue\x18\x02 \x02(\tB\x1d\x92?\x1a\x32\x18\x45numeration string valueR\tenumValue:!\x92?\x1e\x42\x1c\n\x1a\x45numeration type and value\"\xa3\x01\n\x06MsgVal\x12@\n\x07msgType\x18\x01 \x02(\tB&\x92?#2!Fully qualified message type nameR\x07msgType\x12\x38\n\x06keyVal\x18\x02 \x03(\x0b\x32\x10.da.api.KeyValueB\x0e\x92?\x0b\x32\tKey ValueR\x06keyVal:\x1d\x92?\x1a\x42\x18\n\x16Message type and value\"\x8c\x06\n\nTypedValue\x12?\n\x04type\x18\x01 \x02(\x0e\x32\x17.da.api.TypedValue.TypeB\x12\x92?\x0f\x32\rType of valueR\x04type\x12/\n\tstringVal\x18\x02 \x01(\tB\x11\x92?\x0e\x32\x0cString valueR\tstringVal\x12h\n\x11repeatedStringVal\x18\x03 \x03(\tB:\x92?725Value of the item, if the value is a repeated string.R\x11repeatedStringVal\x12;\n\x07\x65numVal\x18\x04 \x01(\x0b\x32\x0f.da.api.EnumValB\x10\x92?\r2\x0b\x45num value.R\x07\x65numVal\x12T\n\x08int64Val\x18\x05 \x01(\x03\x42\x38\x92?523Value of the item, if the value is a 64bit integer.R\x08int64Val\x12T\n\x08int32Val\x18\x06 \x01(\x05\x42\x38\x92?523Value of the item, if the value is a 32bit integer.R\x08int32Val\x12L\n\x07\x62oolVal\x18\x07 \x01(\x08\x42\x32\x92?/2-Value of the item, if the value is a boolean.R\x07\x62oolVal\x12Z\n\x06msgVal\x18\x08 \x01(\x0b\x32\x0e.da.api.MsgValB2\x92?/2-Value of the item, if the value is a message.R\x06msgVal\"g\n\x04Type\x12\n\n\x06STRING\x10\x01\x12\x08\n\x04\x45NUM\x10\x02\x12\t\n\x05INT32\x10\x03\x12\t\n\x05INT64\x10\x04\x12\x08\n\x04\x42OOL\x10\x05\x12\x07\n\x03MSG\x10\x06\x12\x13\n\x0fREPEATED_STRING\x10\x14\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x15:&\x92?#B!\n\x1fValue corresponding to the type\"o\n\x08KeyValue\x12\x1a\n\x03key\x18\x01 \x02(\tB\x08\x92?\x05\x32\x03KeyR\x03key\x12\x30\n\x03val\x18\x02 \x01(\x0b\x32\x12.da.api.TypedValueB\n\x92?\x07\x32\x05ValueR\x03val:\x15\x92?\x12\x42\x10\n\x0eKey value pair')
    ,
    dependencies=[IDL_dot_Protos_dot_Extensions_dot_CustomOptions__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TYPEDVALUE_TYPE = _descriptor.EnumDescriptor(
    name='Type',
    full_name='da.api.TypedValue.Type',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='STRING', index=0, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ENUM', index=1, number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='INT32', index=2, number=3,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='INT64', index=3, number=4,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='BOOL', index=4, number=5,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='MSG', index=5, number=6,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='REPEATED_STRING', index=6, number=20,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='DEFAULT', index=7, number=21,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=1042,
    serialized_end=1145,
)
_sym_db.RegisterEnumDescriptor(_TYPEDVALUE_TYPE)


_ENUMVAL = _descriptor.Descriptor(
    name='EnumVal',
    full_name='da.api.EnumVal',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='enumType', full_name='da.api.EnumVal.enumType', index=0,
            number=1, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0272\025Enumeration type name'))),
        _descriptor.FieldDescriptor(
            name='enumValue', full_name='da.api.EnumVal.enumValue', index=1,
            number=2, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0322\030Enumeration string value'))),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\036B\034\n\032Enumeration type and value')),
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=75,
    serialized_end=236,
)


_MSGVAL = _descriptor.Descriptor(
    name='MsgVal',
    full_name='da.api.MsgVal',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='msgType', full_name='da.api.MsgVal.msgType', index=0,
            number=1, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?#2!Fully qualified message type name'))),
        _descriptor.FieldDescriptor(
            name='keyVal', full_name='da.api.MsgVal.keyVal', index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0132\tKey Value'))),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\032B\030\n\026Message type and value')),
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=239,
    serialized_end=402,
)


_TYPEDVALUE = _descriptor.Descriptor(
    name='TypedValue',
    full_name='da.api.TypedValue',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type', full_name='da.api.TypedValue.type', index=0,
            number=1, type=14, cpp_type=8, label=2,
            has_default_value=False, default_value=1,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0172\rType of value'))),
        _descriptor.FieldDescriptor(
            name='stringVal', full_name='da.api.TypedValue.stringVal', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0162\014String value'))),
        _descriptor.FieldDescriptor(
            name='repeatedStringVal', full_name='da.api.TypedValue.repeatedStringVal', index=2,
            number=3, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?725Value of the item, if the value is a repeated string.'))),
        _descriptor.FieldDescriptor(
            name='enumVal', full_name='da.api.TypedValue.enumVal', index=3,
            number=4, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\r2\013Enum value.'))),
        _descriptor.FieldDescriptor(
            name='int64Val', full_name='da.api.TypedValue.int64Val', index=4,
            number=5, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?523Value of the item, if the value is a 64bit integer.'))),
        _descriptor.FieldDescriptor(
            name='int32Val', full_name='da.api.TypedValue.int32Val', index=5,
            number=6, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?523Value of the item, if the value is a 32bit integer.'))),
        _descriptor.FieldDescriptor(
            name='boolVal', full_name='da.api.TypedValue.boolVal', index=6,
            number=7, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?/2-Value of the item, if the value is a boolean.'))),
        _descriptor.FieldDescriptor(
            name='msgVal', full_name='da.api.TypedValue.msgVal', index=7,
            number=8, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?/2-Value of the item, if the value is a message.'))),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _TYPEDVALUE_TYPE,
    ],
    options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?#B!\n\037Value corresponding to the type')),
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=405,
    serialized_end=1185,
)


_KEYVALUE = _descriptor.Descriptor(
    name='KeyValue',
    full_name='da.api.KeyValue',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='da.api.KeyValue.key', index=0,
            number=1, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0052\003Key'))),
        _descriptor.FieldDescriptor(
            name='val', full_name='da.api.KeyValue.val', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0072\005Value'))),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\022B\020\n\016Key value pair')),
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=1187,
    serialized_end=1298,
)

_MSGVAL.fields_by_name['keyVal'].message_type = _KEYVALUE
_TYPEDVALUE.fields_by_name['type'].enum_type = _TYPEDVALUE_TYPE
_TYPEDVALUE.fields_by_name['enumVal'].message_type = _ENUMVAL
_TYPEDVALUE.fields_by_name['msgVal'].message_type = _MSGVAL
_TYPEDVALUE_TYPE.containing_type = _TYPEDVALUE
_KEYVALUE.fields_by_name['val'].message_type = _TYPEDVALUE
DESCRIPTOR.message_types_by_name['EnumVal'] = _ENUMVAL
DESCRIPTOR.message_types_by_name['MsgVal'] = _MSGVAL
DESCRIPTOR.message_types_by_name['TypedValue'] = _TYPEDVALUE
DESCRIPTOR.message_types_by_name['KeyValue'] = _KEYVALUE

EnumVal = _reflection.GeneratedProtocolMessageType('EnumVal', (_message.Message,), dict(
    DESCRIPTOR = _ENUMVAL,
    __module__ = 'KeyValueTypes_pb2'
    # @@protoc_insertion_point(class_scope:da.api.EnumVal)
    ))
_sym_db.RegisterMessage(EnumVal)

MsgVal = _reflection.GeneratedProtocolMessageType('MsgVal', (_message.Message,), dict(
    DESCRIPTOR = _MSGVAL,
    __module__ = 'KeyValueTypes_pb2'
    # @@protoc_insertion_point(class_scope:da.api.MsgVal)
    ))
_sym_db.RegisterMessage(MsgVal)

TypedValue = _reflection.GeneratedProtocolMessageType('TypedValue', (_message.Message,), dict(
    DESCRIPTOR = _TYPEDVALUE,
    __module__ = 'KeyValueTypes_pb2'
    # @@protoc_insertion_point(class_scope:da.api.TypedValue)
    ))

class _TypedValue_dot_Type(object):
    STRING = 1
    STRING_STRING = "STRING"
    ENUM = 2
    ENUM_STRING = "ENUM"
    INT32 = 3
    INT32_STRING = "INT32"
    INT64 = 4
    INT64_STRING = "INT64"
    BOOL = 5
    BOOL_STRING = "BOOL"
    MSG = 6
    MSG_STRING = "MSG"
    REPEATED_STRING = 20
    REPEATED_STRING_STRING = "REPEATED_STRING"
    DEFAULT = 21
    DEFAULT_STRING = "DEFAULT"
TypedValue.Type = _TypedValue_dot_Type
_sym_db.RegisterMessage(TypedValue)

KeyValue = _reflection.GeneratedProtocolMessageType('KeyValue', (_message.Message,), dict(
    DESCRIPTOR = _KEYVALUE,
    __module__ = 'KeyValueTypes_pb2'
    # @@protoc_insertion_point(class_scope:da.api.KeyValue)
    ))
_sym_db.RegisterMessage(KeyValue)


_ENUMVAL.fields_by_name['enumType'].has_options = True
_ENUMVAL.fields_by_name['enumType']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0272\025Enumeration type name'))
_ENUMVAL.fields_by_name['enumValue'].has_options = True
_ENUMVAL.fields_by_name['enumValue']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0322\030Enumeration string value'))
_ENUMVAL.has_options = True
_ENUMVAL._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\036B\034\n\032Enumeration type and value'))
_MSGVAL.fields_by_name['msgType'].has_options = True
_MSGVAL.fields_by_name['msgType']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?#2!Fully qualified message type name'))
_MSGVAL.fields_by_name['keyVal'].has_options = True
_MSGVAL.fields_by_name['keyVal']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0132\tKey Value'))
_MSGVAL.has_options = True
_MSGVAL._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\032B\030\n\026Message type and value'))
_TYPEDVALUE.fields_by_name['type'].has_options = True
_TYPEDVALUE.fields_by_name['type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0172\rType of value'))
_TYPEDVALUE.fields_by_name['stringVal'].has_options = True
_TYPEDVALUE.fields_by_name['stringVal']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0162\014String value'))
_TYPEDVALUE.fields_by_name['repeatedStringVal'].has_options = True
_TYPEDVALUE.fields_by_name['repeatedStringVal']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?725Value of the item, if the value is a repeated string.'))
_TYPEDVALUE.fields_by_name['enumVal'].has_options = True
_TYPEDVALUE.fields_by_name['enumVal']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\r2\013Enum value.'))
_TYPEDVALUE.fields_by_name['int64Val'].has_options = True
_TYPEDVALUE.fields_by_name['int64Val']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?523Value of the item, if the value is a 64bit integer.'))
_TYPEDVALUE.fields_by_name['int32Val'].has_options = True
_TYPEDVALUE.fields_by_name['int32Val']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?523Value of the item, if the value is a 32bit integer.'))
_TYPEDVALUE.fields_by_name['boolVal'].has_options = True
_TYPEDVALUE.fields_by_name['boolVal']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?/2-Value of the item, if the value is a boolean.'))
_TYPEDVALUE.fields_by_name['msgVal'].has_options = True
_TYPEDVALUE.fields_by_name['msgVal']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?/2-Value of the item, if the value is a message.'))
_TYPEDVALUE.has_options = True
_TYPEDVALUE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?#B!\n\037Value corresponding to the type'))
_KEYVALUE.fields_by_name['key'].has_options = True
_KEYVALUE.fields_by_name['key']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0052\003Key'))
_KEYVALUE.fields_by_name['val'].has_options = True
_KEYVALUE.fields_by_name['val']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0072\005Value'))
_KEYVALUE.has_options = True
_KEYVALUE._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\022B\020\n\016Key value pair'))
# @@protoc_insertion_point(module_scope)