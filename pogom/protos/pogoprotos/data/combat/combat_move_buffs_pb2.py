# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/combat/combat_move_buffs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/combat/combat_move_buffs.proto',
  package='pogoprotos.data.combat',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n.pogoprotos/data/combat/combat_move_buffs.proto\x12\x16pogoprotos.data.combat\"\xbb\x01\n\x0f\x43ombatMoveBuffs\x12)\n!attacker_attack_stat_stage_change\x18\x01 \x01(\x05\x12*\n\"attacker_defense_stat_stage_change\x18\x02 \x01(\x05\x12\'\n\x1ftarget_attack_stat_stage_change\x18\x03 \x01(\x05\x12(\n target_defense_stat_stage_change\x18\x04 \x01(\x05\x62\x06proto3')
)




_COMBATMOVEBUFFS = _descriptor.Descriptor(
  name='CombatMoveBuffs',
  full_name='pogoprotos.data.combat.CombatMoveBuffs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attacker_attack_stat_stage_change', full_name='pogoprotos.data.combat.CombatMoveBuffs.attacker_attack_stat_stage_change', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attacker_defense_stat_stage_change', full_name='pogoprotos.data.combat.CombatMoveBuffs.attacker_defense_stat_stage_change', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_attack_stat_stage_change', full_name='pogoprotos.data.combat.CombatMoveBuffs.target_attack_stat_stage_change', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_defense_stat_stage_change', full_name='pogoprotos.data.combat.CombatMoveBuffs.target_defense_stat_stage_change', index=3,
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
  serialized_start=75,
  serialized_end=262,
)

DESCRIPTOR.message_types_by_name['CombatMoveBuffs'] = _COMBATMOVEBUFFS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatMoveBuffs = _reflection.GeneratedProtocolMessageType('CombatMoveBuffs', (_message.Message,), dict(
  DESCRIPTOR = _COMBATMOVEBUFFS,
  __module__ = 'pogoprotos.data.combat.combat_move_buffs_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.CombatMoveBuffs)
  ))
_sym_db.RegisterMessage(CombatMoveBuffs)


# @@protoc_insertion_point(module_scope)
