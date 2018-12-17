# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/onboarding_v2_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/onboarding_v2_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n7pogoprotos/settings/master/onboarding_v2_settings.proto\x12\x1apogoprotos.settings.master\x1a!pogoprotos/enums/pokemon_id.proto\"\xbe\x01\n\x14OnboardingV2Settings\x12\x1c\n\x14\x65nable_onboarding_v2\x18\x01 \x01(\x08\x12/\n\npokedex_id\x18\x02 \x03(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12;\n\x16onboarding_egg_pokemon\x18\x03 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x1a\n\x12\x65gg_km_until_hatch\x18\x04 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,])




_ONBOARDINGV2SETTINGS = _descriptor.Descriptor(
  name='OnboardingV2Settings',
  full_name='pogoprotos.settings.master.OnboardingV2Settings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable_onboarding_v2', full_name='pogoprotos.settings.master.OnboardingV2Settings.enable_onboarding_v2', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pokedex_id', full_name='pogoprotos.settings.master.OnboardingV2Settings.pokedex_id', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='onboarding_egg_pokemon', full_name='pogoprotos.settings.master.OnboardingV2Settings.onboarding_egg_pokemon', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='egg_km_until_hatch', full_name='pogoprotos.settings.master.OnboardingV2Settings.egg_km_until_hatch', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=123,
  serialized_end=313,
)

_ONBOARDINGV2SETTINGS.fields_by_name['pokedex_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_ONBOARDINGV2SETTINGS.fields_by_name['onboarding_egg_pokemon'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
DESCRIPTOR.message_types_by_name['OnboardingV2Settings'] = _ONBOARDINGV2SETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OnboardingV2Settings = _reflection.GeneratedProtocolMessageType('OnboardingV2Settings', (_message.Message,), dict(
  DESCRIPTOR = _ONBOARDINGV2SETTINGS,
  __module__ = 'pogoprotos.settings.master.onboarding_v2_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.OnboardingV2Settings)
  ))
_sym_db.RegisterMessage(OnboardingV2Settings)


# @@protoc_insertion_point(module_scope)
