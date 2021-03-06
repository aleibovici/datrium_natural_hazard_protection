# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RenderedTask.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from IDL.Protos.Extensions import CustomOptions_pb2 as IDL_dot_Protos_dot_Extensions_dot_CustomOptions__pb2
from IDL.Protos.Extensions import APIException_pb2 as IDL_dot_Protos_dot_Extensions_dot_APIException__pb2
from SysMgmt.Api.IDL.Main import KeyValueTypes_pb2 as SysMgmt_dot_Api_dot_IDL_dot_Main_dot_KeyValueTypes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name='RenderedTask.proto',
    package='da.api.task',
    syntax='proto2',
    serialized_pb=_b('\n\x12RenderedTask.proto\x12\x0b\x64\x61.api.task\x1a)IDL/Protos/Extensions/CustomOptions.proto\x1a(IDL/Protos/Extensions/APIException.proto\x1a(SysMgmt/Api/IDL/Main/KeyValueTypes.proto\"\xa5\x04\n\x04Task\x12\x17\n\x02id\x18\x01 \x02(\tB\x07\x92?\x04\x32\x02IDR\x02id\x12\x39\n\tstartTime\x18\x02 \x01(\x04\x42\x1b\x92?\x18\x32\x16Start time of the taskR\tstartTime\x12%\n\x05state\x18\x03 \x02(\tB\x0f\x92?\x0c\x32\nTask stateR\x05state\x12-\n\x08progress\x18\x04 \x02(\rB\x11\x92?\x0e\x32\x0cProgress (%)R\x08progress\x12L\n\x16\x65xpectedCompletionTime\x18\x05 \x01(\x04\x42\x14\x92?\x11\x32\x0f\x45TA of the taskR\x16\x65xpectedCompletionTime\x12\x41\n\x0e\x63ompletionTime\x18\x06 \x01(\x04\x42\x19\x92?\x16\x32\x14\x45nd time of the taskR\x0e\x63ompletionTime\x12M\n\x05\x65rror\x18\x07 \x01(\x0b\x32\x15.da.core.DvxExceptionB \x92?\x1d\x32\x1b\x45rror during task executionR\x05\x65rror\x12\x85\x01\n\tkeyValues\x18\x08 \x03(\x0b\x32\x10.da.api.KeyValueBU\x92?R2PKey value associated with the task. This is only available after task completionR\tkeyValues:\x0b\x92?\x08\x42\x06\n\x04Task*f\n\tTaskState\x12\n\n\x06QUEUED\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\x12\x0b\n\x07SUCCESS\x10\x04\x12\x0e\n\nCANCELLING\x10\x05\x12\x0c\n\x08\x43\x41NCELED\x10\x06\x12\n\n\x06PAUSED\x10\x07')
    ,
    dependencies=[IDL_dot_Protos_dot_Extensions_dot_CustomOptions__pb2.DESCRIPTOR,IDL_dot_Protos_dot_Extensions_dot_APIException__pb2.DESCRIPTOR,SysMgmt_dot_Api_dot_IDL_dot_Main_dot_KeyValueTypes__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_TASKSTATE = _descriptor.EnumDescriptor(
    name='TaskState',
    full_name='da.api.task.TaskState',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='QUEUED', index=0, number=1,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='RUNNING', index=1, number=2,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='ERROR', index=2, number=3,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='SUCCESS', index=3, number=4,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CANCELLING', index=4, number=5,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='CANCELED', index=5, number=6,
            options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='PAUSED', index=6, number=7,
            options=None,
            type=None),
    ],
    containing_type=None,
    options=None,
    serialized_start=714,
    serialized_end=816,
)
_sym_db.RegisterEnumDescriptor(_TASKSTATE)


class TaskState(object):
    QUEUED = 1
    QUEUED_STRING = "QUEUED"
    RUNNING = 2
    RUNNING_STRING = "RUNNING"
    ERROR = 3
    ERROR_STRING = "ERROR"
    SUCCESS = 4
    SUCCESS_STRING = "SUCCESS"
    CANCELLING = 5
    CANCELLING_STRING = "CANCELLING"
    CANCELED = 6
    CANCELED_STRING = "CANCELED"
    PAUSED = 7
    PAUSED_STRING = "PAUSED"

QUEUED = 1
RUNNING = 2
ERROR = 3
SUCCESS = 4
CANCELLING = 5
CANCELED = 6
PAUSED = 7



_TASK = _descriptor.Descriptor(
    name='Task',
    full_name='da.api.task.Task',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='da.api.task.Task.id', index=0,
            number=1, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0042\002ID'))),
        _descriptor.FieldDescriptor(
            name='startTime', full_name='da.api.task.Task.startTime', index=1,
            number=2, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0302\026Start time of the task'))),
        _descriptor.FieldDescriptor(
            name='state', full_name='da.api.task.Task.state', index=2,
            number=3, type=9, cpp_type=9, label=2,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0142\nTask state'))),
        _descriptor.FieldDescriptor(
            name='progress', full_name='da.api.task.Task.progress', index=3,
            number=4, type=13, cpp_type=3, label=2,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0162\014Progress (%)'))),
        _descriptor.FieldDescriptor(
            name='expectedCompletionTime', full_name='da.api.task.Task.expectedCompletionTime', index=4,
            number=5, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0212\017ETA of the task'))),
        _descriptor.FieldDescriptor(
            name='completionTime', full_name='da.api.task.Task.completionTime', index=5,
            number=6, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0262\024End time of the task'))),
        _descriptor.FieldDescriptor(
            name='error', full_name='da.api.task.Task.error', index=6,
            number=7, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0352\033Error during task execution'))),
        _descriptor.FieldDescriptor(
            name='keyValues', full_name='da.api.task.Task.keyValues', index=7,
            number=8, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?R2PKey value associated with the task. This is only available after task completion'))),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\010B\006\n\004Task')),
    is_extendable=False,
    syntax='proto2',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=163,
    serialized_end=712,
)

_TASK.fields_by_name['error'].message_type = IDL_dot_Protos_dot_Extensions_dot_APIException__pb2._DVXEXCEPTION
_TASK.fields_by_name['keyValues'].message_type = SysMgmt_dot_Api_dot_IDL_dot_Main_dot_KeyValueTypes__pb2._KEYVALUE
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.enum_types_by_name['TaskState'] = _TASKSTATE

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), dict(
    DESCRIPTOR = _TASK,
    __module__ = 'RenderedTask_pb2'
    # @@protoc_insertion_point(class_scope:da.api.task.Task)
    ))
_sym_db.RegisterMessage(Task)


_TASK.fields_by_name['id'].has_options = True
_TASK.fields_by_name['id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0042\002ID'))
_TASK.fields_by_name['startTime'].has_options = True
_TASK.fields_by_name['startTime']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0302\026Start time of the task'))
_TASK.fields_by_name['state'].has_options = True
_TASK.fields_by_name['state']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0142\nTask state'))
_TASK.fields_by_name['progress'].has_options = True
_TASK.fields_by_name['progress']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0162\014Progress (%)'))
_TASK.fields_by_name['expectedCompletionTime'].has_options = True
_TASK.fields_by_name['expectedCompletionTime']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0212\017ETA of the task'))
_TASK.fields_by_name['completionTime'].has_options = True
_TASK.fields_by_name['completionTime']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0262\024End time of the task'))
_TASK.fields_by_name['error'].has_options = True
_TASK.fields_by_name['error']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?\0352\033Error during task execution'))
_TASK.fields_by_name['keyValues'].has_options = True
_TASK.fields_by_name['keyValues']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\222?R2PKey value associated with the task. This is only available after task completion'))
_TASK.has_options = True
_TASK._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('\222?\010B\006\n\004Task'))
# @@protoc_insertion_point(module_scope)
