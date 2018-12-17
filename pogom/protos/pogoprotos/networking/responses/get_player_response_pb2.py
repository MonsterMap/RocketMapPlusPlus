# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_player_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import player_data_pb2 as pogoprotos_dot_data_dot_player__data__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_player_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n9pogoprotos/networking/responses/get_player_response.proto\x12\x1fpogoprotos.networking.responses\x1a!pogoprotos/data/player_data.proto\"\x9c\x02\n\x11GetPlayerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x30\n\x0bplayer_data\x18\x02 \x01(\x0b\x32\x1b.pogoprotos.data.PlayerData\x12\x0e\n\x06\x62\x61nned\x18\x03 \x01(\x08\x12\x0c\n\x04warn\x18\x04 \x01(\x08\x12\x13\n\x0bwas_created\x18\x05 \x01(\x08\x12!\n\x19warn_message_acknowledged\x18\x06 \x01(\x08\x12\x15\n\rwas_suspended\x18\x07 \x01(\x08\x12&\n\x1esuspended_message_acknowledged\x18\x08 \x01(\x08\x12\x16\n\x0ewarn_expire_ms\x18\t \x01(\x03\x12\x17\n\x0fuser_permission\x18\n \x03(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_player__data__pb2.DESCRIPTOR,])




_GETPLAYERRESPONSE = _descriptor.Descriptor(
  name='GetPlayerResponse',
  full_name='pogoprotos.networking.responses.GetPlayerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='pogoprotos.networking.responses.GetPlayerResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_data', full_name='pogoprotos.networking.responses.GetPlayerResponse.player_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='banned', full_name='pogoprotos.networking.responses.GetPlayerResponse.banned', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warn', full_name='pogoprotos.networking.responses.GetPlayerResponse.warn', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='was_created', full_name='pogoprotos.networking.responses.GetPlayerResponse.was_created', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warn_message_acknowledged', full_name='pogoprotos.networking.responses.GetPlayerResponse.warn_message_acknowledged', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='was_suspended', full_name='pogoprotos.networking.responses.GetPlayerResponse.was_suspended', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suspended_message_acknowledged', full_name='pogoprotos.networking.responses.GetPlayerResponse.suspended_message_acknowledged', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='warn_expire_ms', full_name='pogoprotos.networking.responses.GetPlayerResponse.warn_expire_ms', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_permission', full_name='pogoprotos.networking.responses.GetPlayerResponse.user_permission', index=9,
      number=10, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=130,
  serialized_end=414,
)

_GETPLAYERRESPONSE.fields_by_name['player_data'].message_type = pogoprotos_dot_data_dot_player__data__pb2._PLAYERDATA
DESCRIPTOR.message_types_by_name['GetPlayerResponse'] = _GETPLAYERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetPlayerResponse = _reflection.GeneratedProtocolMessageType('GetPlayerResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPLAYERRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_player_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetPlayerResponse)
  ))
_sym_db.RegisterMessage(GetPlayerResponse)


# @@protoc_insertion_point(module_scope)
