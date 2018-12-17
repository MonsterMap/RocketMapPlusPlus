# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/player/user_attributes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/player/user_attributes.proto',
  package='pogoprotos.data.player',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,pogoprotos/data/player/user_attributes.proto\x12\x16pogoprotos.data.player\"\x87\x01\n\x0eUserAttributes\x12\r\n\x05level\x18\x01 \x01(\x05\x12\x15\n\rxp_percentage\x18\x02 \x01(\x03\x12\x16\n\x0epokecoin_count\x18\x03 \x01(\x03\x12\x0c\n\x04team\x18\x04 \x01(\x05\x12\x14\n\x0c\x63\x61tch_streak\x18\x05 \x01(\x05\x12\x13\n\x0bspin_streak\x18\x06 \x01(\x05\x62\x06proto3')
)




_USERATTRIBUTES = _descriptor.Descriptor(
  name='UserAttributes',
  full_name='pogoprotos.data.player.UserAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='pogoprotos.data.player.UserAttributes.level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xp_percentage', full_name='pogoprotos.data.player.UserAttributes.xp_percentage', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokecoin_count', full_name='pogoprotos.data.player.UserAttributes.pokecoin_count', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='team', full_name='pogoprotos.data.player.UserAttributes.team', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='catch_streak', full_name='pogoprotos.data.player.UserAttributes.catch_streak', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spin_streak', full_name='pogoprotos.data.player.UserAttributes.spin_streak', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=73,
  serialized_end=208,
)

DESCRIPTOR.message_types_by_name['UserAttributes'] = _USERATTRIBUTES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserAttributes = _reflection.GeneratedProtocolMessageType('UserAttributes', (_message.Message,), dict(
  DESCRIPTOR = _USERATTRIBUTES,
  __module__ = 'pogoprotos.data.player.user_attributes_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.player.UserAttributes)
  ))
_sym_db.RegisterMessage(UserAttributes)


# @@protoc_insertion_point(module_scope)
