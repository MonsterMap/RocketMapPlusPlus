# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/platform_client_action.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/platform_client_action.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-pogoprotos/enums/platform_client_action.proto\x12\x10pogoprotos.enums*\xa9\x08\n\x14PlatformClientAction\x12\"\n\x1eUNKNOWN_PLATFORM_CLIENT_ACTION\x10\x00\x12\x1f\n\x1aREGISTER_PUSH_NOTIFICATION\x10\x88\'\x12!\n\x1cUNREGISTER_PUSH_NOTIFICATION\x10\x89\'\x12\x1f\n\x1aUPDATE_NOTIFICATION_STATUS\x10\x8a\'\x12\'\n\"OPT_OUT_PUSH_NOTIFICATION_CATEGORY\x10\x8b\'\x12#\n\x1e\x44OWNLOAD_GAME_MASTER_TEMPLATES\x10\x8c\'\x12\x12\n\rGET_INVENTORY\x10\x8d\'\x12\x14\n\x0fREDEEM_PASSCODE\x10\x8e\'\x12\t\n\x04PING\x10\x8f\'\x12\x15\n\x10\x41\x44\x44_LOGIN_ACTION\x10\x90\'\x12\x18\n\x13REMOVE_LOGIN_ACTION\x10\x91\'\x12\x16\n\x11LIST_LOGIN_ACTION\x10\x92\'\x12\x10\n\x0b\x41\x44\x44_NEW_POI\x10\x93\'\x12\x18\n\x13PROXY_SOCIAL_ACTION\x10\x94\'\x12\x15\n\x10\x43LIENT_TELEMETRY\x10\x95\'\x12\x1e\n\x19GET_AVAILABLE_SUBMISSIONS\x10\x96\'\x12$\n\x1fGET_SIGNED_URL_FOR_PHOTO_UPLOAD\x10\x97\'\x12\x19\n\x14REPLACE_LOGIN_ACTION\x10\x98\'\x12%\n PROXY_SOCIAL_SIDE_CHANNEL_ACTION\x10\x99\'\x12\x1d\n\x18\x43OLLECT_CLIENT_TELEMETRY\x10\x9a\'\x12\x11\n\x0cPURCHASE_SKU\x10\x9b\'\x12$\n\x1fGET_AVAILABLE_SKUS_AND_BALANCES\x10\x9c\'\x12\x1a\n\x15REDEEM_GOOGLE_RECEIPT\x10\x9d\'\x12\x19\n\x14REDEEM_APPLE_RECEIPT\x10\x9e\'\x12\x1b\n\x16REDEEM_DESKTOP_RECEIPT\x10\x9f\'\x12\x1b\n\x16UPDATE_FITNESS_METRICS\x10\xa0\'\x12\x17\n\x12GET_FITNESS_REPORT\x10\xa1\'\x12\"\n\x1dGET_CLIENT_TELEMETRY_SETTINGS\x10\xa2\'\x12\x0f\n\nPING_ASYNC\x10\xa3\'\x12 \n\x1bREGISTER_BACKGROUND_SERVICE\x10\xa4\'\x12\x1f\n\x1aGET_CLIENT_BGMODE_SETTINGS\x10\xa5\'\x12\x14\n\x0fPING_DOWNSTREAM\x10\xa6\'\x12\'\n\"SET_IN_GAME_CURRENCY_EXCHANGE_RATE\x10\xa8\'\x12\x1d\n\x18REQUEST_GEOFENCE_UPDATES\x10\xa9\'\x12\x1b\n\x16UPDATE_PLAYER_LOCATION\x10\xaa\'\x12\x1c\n\x17PROFANITY_FILTER_ACTION\x10\xab\'b\x06proto3')
)

_PLATFORMCLIENTACTION = _descriptor.EnumDescriptor(
  name='PlatformClientAction',
  full_name='pogoprotos.enums.PlatformClientAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_PLATFORM_CLIENT_ACTION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_PUSH_NOTIFICATION', index=1, number=5000,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNREGISTER_PUSH_NOTIFICATION', index=2, number=5001,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_NOTIFICATION_STATUS', index=3, number=5002,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPT_OUT_PUSH_NOTIFICATION_CATEGORY', index=4, number=5003,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD_GAME_MASTER_TEMPLATES', index=5, number=5004,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_INVENTORY', index=6, number=5005,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDEEM_PASSCODE', index=7, number=5006,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PING', index=8, number=5007,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_LOGIN_ACTION', index=9, number=5008,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_LOGIN_ACTION', index=10, number=5009,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIST_LOGIN_ACTION', index=11, number=5010,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_NEW_POI', index=12, number=5011,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROXY_SOCIAL_ACTION', index=13, number=5012,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_TELEMETRY', index=14, number=5013,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_AVAILABLE_SUBMISSIONS', index=15, number=5014,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_SIGNED_URL_FOR_PHOTO_UPLOAD', index=16, number=5015,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLACE_LOGIN_ACTION', index=17, number=5016,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROXY_SOCIAL_SIDE_CHANNEL_ACTION', index=18, number=5017,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECT_CLIENT_TELEMETRY', index=19, number=5018,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PURCHASE_SKU', index=20, number=5019,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_AVAILABLE_SKUS_AND_BALANCES', index=21, number=5020,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDEEM_GOOGLE_RECEIPT', index=22, number=5021,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDEEM_APPLE_RECEIPT', index=23, number=5022,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDEEM_DESKTOP_RECEIPT', index=24, number=5023,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_FITNESS_METRICS', index=25, number=5024,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_FITNESS_REPORT', index=26, number=5025,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_CLIENT_TELEMETRY_SETTINGS', index=27, number=5026,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PING_ASYNC', index=28, number=5027,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER_BACKGROUND_SERVICE', index=29, number=5028,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GET_CLIENT_BGMODE_SETTINGS', index=30, number=5029,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PING_DOWNSTREAM', index=31, number=5030,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_IN_GAME_CURRENCY_EXCHANGE_RATE', index=32, number=5032,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_GEOFENCE_UPDATES', index=33, number=5033,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_PLAYER_LOCATION', index=34, number=5034,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROFANITY_FILTER_ACTION', index=35, number=5035,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=68,
  serialized_end=1133,
)
_sym_db.RegisterEnumDescriptor(_PLATFORMCLIENTACTION)

PlatformClientAction = enum_type_wrapper.EnumTypeWrapper(_PLATFORMCLIENTACTION)
UNKNOWN_PLATFORM_CLIENT_ACTION = 0
REGISTER_PUSH_NOTIFICATION = 5000
UNREGISTER_PUSH_NOTIFICATION = 5001
UPDATE_NOTIFICATION_STATUS = 5002
OPT_OUT_PUSH_NOTIFICATION_CATEGORY = 5003
DOWNLOAD_GAME_MASTER_TEMPLATES = 5004
GET_INVENTORY = 5005
REDEEM_PASSCODE = 5006
PING = 5007
ADD_LOGIN_ACTION = 5008
REMOVE_LOGIN_ACTION = 5009
LIST_LOGIN_ACTION = 5010
ADD_NEW_POI = 5011
PROXY_SOCIAL_ACTION = 5012
CLIENT_TELEMETRY = 5013
GET_AVAILABLE_SUBMISSIONS = 5014
GET_SIGNED_URL_FOR_PHOTO_UPLOAD = 5015
REPLACE_LOGIN_ACTION = 5016
PROXY_SOCIAL_SIDE_CHANNEL_ACTION = 5017
COLLECT_CLIENT_TELEMETRY = 5018
PURCHASE_SKU = 5019
GET_AVAILABLE_SKUS_AND_BALANCES = 5020
REDEEM_GOOGLE_RECEIPT = 5021
REDEEM_APPLE_RECEIPT = 5022
REDEEM_DESKTOP_RECEIPT = 5023
UPDATE_FITNESS_METRICS = 5024
GET_FITNESS_REPORT = 5025
GET_CLIENT_TELEMETRY_SETTINGS = 5026
PING_ASYNC = 5027
REGISTER_BACKGROUND_SERVICE = 5028
GET_CLIENT_BGMODE_SETTINGS = 5029
PING_DOWNSTREAM = 5030
SET_IN_GAME_CURRENCY_EXCHANGE_RATE = 5032
REQUEST_GEOFENCE_UPDATES = 5033
UPDATE_PLAYER_LOCATION = 5034
PROFANITY_FILTER_ACTION = 5035


DESCRIPTOR.enum_types_by_name['PlatformClientAction'] = _PLATFORMCLIENTACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
