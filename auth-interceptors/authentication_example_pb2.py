# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authentication_example.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='authentication_example.proto',
  package='pyconke.example.authetication',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1c\x61uthentication_example.proto\x12\x1dpyconke.example.authetication\" \n\x0cHelloRequest\x12\x10\n\x08greeting\x18\x01 \x01(\t\"\x1e\n\rHelloResponse\x12\r\n\x05reply\x18\x01 \x01(\t2u\n\x0cHelloService\x12\x65\n\x08SayHello\x12+.pyconke.example.authetication.HelloRequest\x1a,.pyconke.example.authetication.HelloResponseb\x06proto3')
)




_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='pyconke.example.authetication.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='pyconke.example.authetication.HelloRequest.greeting', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=95,
)


_HELLORESPONSE = _descriptor.Descriptor(
  name='HelloResponse',
  full_name='pyconke.example.authetication.HelloResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='pyconke.example.authetication.HelloResponse.reply', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=127,
)

DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloResponse'] = _HELLORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), dict(
  DESCRIPTOR = _HELLOREQUEST,
  __module__ = 'authentication_example_pb2'
  # @@protoc_insertion_point(class_scope:pyconke.example.authetication.HelloRequest)
  ))
_sym_db.RegisterMessage(HelloRequest)

HelloResponse = _reflection.GeneratedProtocolMessageType('HelloResponse', (_message.Message,), dict(
  DESCRIPTOR = _HELLORESPONSE,
  __module__ = 'authentication_example_pb2'
  # @@protoc_insertion_point(class_scope:pyconke.example.authetication.HelloResponse)
  ))
_sym_db.RegisterMessage(HelloResponse)



_HELLOSERVICE = _descriptor.ServiceDescriptor(
  name='HelloService',
  full_name='pyconke.example.authetication.HelloService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=129,
  serialized_end=246,
  methods=[
  _descriptor.MethodDescriptor(
    name='SayHello',
    full_name='pyconke.example.authetication.HelloService.SayHello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLORESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HELLOSERVICE)

DESCRIPTOR.services_by_name['HelloService'] = _HELLOSERVICE

# @@protoc_insertion_point(module_scope)
