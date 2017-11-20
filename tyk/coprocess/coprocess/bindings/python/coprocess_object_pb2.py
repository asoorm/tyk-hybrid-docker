# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: coprocess_object.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import coprocess_mini_request_object_pb2 as coprocess__mini__request__object__pb2
import coprocess_session_state_pb2 as coprocess__session__state__pb2
import coprocess_common_pb2 as coprocess__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='coprocess_object.proto',
  package='coprocess',
  syntax='proto3',
  serialized_pb=_b('\n\x16\x63oprocess_object.proto\x12\tcoprocess\x1a#coprocess_mini_request_object.proto\x1a\x1d\x63oprocess_session_state.proto\x1a\x16\x63oprocess_common.proto\"\xd8\x02\n\x06Object\x12&\n\thook_type\x18\x01 \x01(\x0e\x32\x13.coprocess.HookType\x12\x11\n\thook_name\x18\x02 \x01(\t\x12-\n\x07request\x18\x03 \x01(\x0b\x32\x1c.coprocess.MiniRequestObject\x12(\n\x07session\x18\x04 \x01(\x0b\x32\x17.coprocess.SessionState\x12\x31\n\x08metadata\x18\x05 \x03(\x0b\x32\x1f.coprocess.Object.MetadataEntry\x12)\n\x04spec\x18\x06 \x03(\x0b\x32\x1b.coprocess.Object.SpecEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a+\n\tSpecEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x18\n\x05\x45vent\x12\x0f\n\x07payload\x18\x01 \x01(\t\"\x0c\n\nEventReply2|\n\nDispatcher\x12\x32\n\x08\x44ispatch\x12\x11.coprocess.Object\x1a\x11.coprocess.Object\"\x00\x12:\n\rDispatchEvent\x12\x10.coprocess.Event\x1a\x15.coprocess.EventReply\"\x00\x62\x06proto3')
  ,
  dependencies=[coprocess__mini__request__object__pb2.DESCRIPTOR,coprocess__session__state__pb2.DESCRIPTOR,coprocess__common__pb2.DESCRIPTOR,])




_OBJECT_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='coprocess.Object.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='coprocess.Object.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='coprocess.Object.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=382,
  serialized_end=429,
)

_OBJECT_SPECENTRY = _descriptor.Descriptor(
  name='SpecEntry',
  full_name='coprocess.Object.SpecEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='coprocess.Object.SpecEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='coprocess.Object.SpecEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=431,
  serialized_end=474,
)

_OBJECT = _descriptor.Descriptor(
  name='Object',
  full_name='coprocess.Object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hook_type', full_name='coprocess.Object.hook_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hook_name', full_name='coprocess.Object.hook_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request', full_name='coprocess.Object.request', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='coprocess.Object.session', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='coprocess.Object.metadata', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spec', full_name='coprocess.Object.spec', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_OBJECT_METADATAENTRY, _OBJECT_SPECENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=474,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='coprocess.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='coprocess.Event.payload', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=476,
  serialized_end=500,
)


_EVENTREPLY = _descriptor.Descriptor(
  name='EventReply',
  full_name='coprocess.EventReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=514,
)

_OBJECT_METADATAENTRY.containing_type = _OBJECT
_OBJECT_SPECENTRY.containing_type = _OBJECT
_OBJECT.fields_by_name['hook_type'].enum_type = coprocess__common__pb2._HOOKTYPE
_OBJECT.fields_by_name['request'].message_type = coprocess__mini__request__object__pb2._MINIREQUESTOBJECT
_OBJECT.fields_by_name['session'].message_type = coprocess__session__state__pb2._SESSIONSTATE
_OBJECT.fields_by_name['metadata'].message_type = _OBJECT_METADATAENTRY
_OBJECT.fields_by_name['spec'].message_type = _OBJECT_SPECENTRY
DESCRIPTOR.message_types_by_name['Object'] = _OBJECT
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['EventReply'] = _EVENTREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), dict(

  MetadataEntry = _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), dict(
    DESCRIPTOR = _OBJECT_METADATAENTRY,
    __module__ = 'coprocess_object_pb2'
    # @@protoc_insertion_point(class_scope:coprocess.Object.MetadataEntry)
    ))
  ,

  SpecEntry = _reflection.GeneratedProtocolMessageType('SpecEntry', (_message.Message,), dict(
    DESCRIPTOR = _OBJECT_SPECENTRY,
    __module__ = 'coprocess_object_pb2'
    # @@protoc_insertion_point(class_scope:coprocess.Object.SpecEntry)
    ))
  ,
  DESCRIPTOR = _OBJECT,
  __module__ = 'coprocess_object_pb2'
  # @@protoc_insertion_point(class_scope:coprocess.Object)
  ))
_sym_db.RegisterMessage(Object)
_sym_db.RegisterMessage(Object.MetadataEntry)
_sym_db.RegisterMessage(Object.SpecEntry)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'coprocess_object_pb2'
  # @@protoc_insertion_point(class_scope:coprocess.Event)
  ))
_sym_db.RegisterMessage(Event)

EventReply = _reflection.GeneratedProtocolMessageType('EventReply', (_message.Message,), dict(
  DESCRIPTOR = _EVENTREPLY,
  __module__ = 'coprocess_object_pb2'
  # @@protoc_insertion_point(class_scope:coprocess.EventReply)
  ))
_sym_db.RegisterMessage(EventReply)


_OBJECT_METADATAENTRY.has_options = True
_OBJECT_METADATAENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_OBJECT_SPECENTRY.has_options = True
_OBJECT_SPECENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class DispatcherStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Dispatch = channel.unary_unary(
          '/coprocess.Dispatcher/Dispatch',
          request_serializer=Object.SerializeToString,
          response_deserializer=Object.FromString,
          )
      self.DispatchEvent = channel.unary_unary(
          '/coprocess.Dispatcher/DispatchEvent',
          request_serializer=Event.SerializeToString,
          response_deserializer=EventReply.FromString,
          )


  class DispatcherServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def Dispatch(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def DispatchEvent(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_DispatcherServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Dispatch': grpc.unary_unary_rpc_method_handler(
            servicer.Dispatch,
            request_deserializer=Object.FromString,
            response_serializer=Object.SerializeToString,
        ),
        'DispatchEvent': grpc.unary_unary_rpc_method_handler(
            servicer.DispatchEvent,
            request_deserializer=Event.FromString,
            response_serializer=EventReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'coprocess.Dispatcher', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaDispatcherServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def Dispatch(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def DispatchEvent(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaDispatcherStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def Dispatch(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    Dispatch.future = None
    def DispatchEvent(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    DispatchEvent.future = None


  def beta_create_Dispatcher_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('coprocess.Dispatcher', 'Dispatch'): Object.FromString,
      ('coprocess.Dispatcher', 'DispatchEvent'): Event.FromString,
    }
    response_serializers = {
      ('coprocess.Dispatcher', 'Dispatch'): Object.SerializeToString,
      ('coprocess.Dispatcher', 'DispatchEvent'): EventReply.SerializeToString,
    }
    method_implementations = {
      ('coprocess.Dispatcher', 'Dispatch'): face_utilities.unary_unary_inline(servicer.Dispatch),
      ('coprocess.Dispatcher', 'DispatchEvent'): face_utilities.unary_unary_inline(servicer.DispatchEvent),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Dispatcher_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('coprocess.Dispatcher', 'Dispatch'): Object.SerializeToString,
      ('coprocess.Dispatcher', 'DispatchEvent'): Event.SerializeToString,
    }
    response_deserializers = {
      ('coprocess.Dispatcher', 'Dispatch'): Object.FromString,
      ('coprocess.Dispatcher', 'DispatchEvent'): EventReply.FromString,
    }
    cardinalities = {
      'Dispatch': cardinality.Cardinality.UNARY_UNARY,
      'DispatchEvent': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'coprocess.Dispatcher', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)