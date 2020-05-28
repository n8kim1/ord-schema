# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ord-schema/proto/test.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ord-schema/proto/test.proto',
  package='ord_test',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1bord-schema/proto/test.proto\x12\x08ord_test\"r\n\x06Scalar\x12\x13\n\x0bint32_value\x18\x01 \x01(\x05\x12\x13\n\x0bint64_value\x18\x02 \x01(\x03\x12\x13\n\x0b\x66loat_value\x18\x03 \x01(\x02\x12\x14\n\x0cstring_value\x18\x04 \x01(\t\x12\x13\n\x0b\x62ytes_value\x18\x05 \x01(\x0c\" \n\x0eRepeatedScalar\x12\x0e\n\x06values\x18\x01 \x03(\x02\"f\n\x04\x45num\x12(\n\x05value\x18\x01 \x01(\x0e\x32\x19.ord_test.Enum.EnumValues\"4\n\nEnumValues\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\t\n\x05\x46IRST\x10\x01\x12\n\n\x06SECOND\x10\x02\"w\n\x0cRepeatedEnum\x12\x31\n\x06values\x18\x01 \x03(\x0e\x32!.ord_test.RepeatedEnum.EnumValues\"4\n\nEnumValues\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\t\n\x05\x46IRST\x10\x01\x12\n\n\x06SECOND\x10\x02\"G\n\x06Nested\x12%\n\x05\x63hild\x18\x01 \x01(\x0b\x32\x16.ord_test.Nested.Child\x1a\x16\n\x05\x43hild\x12\r\n\x05value\x18\x01 \x01(\x02\"Z\n\x0eRepeatedNested\x12\x30\n\x08\x63hildren\x18\x01 \x03(\x0b\x32\x1e.ord_test.RepeatedNested.Child\x1a\x16\n\x05\x43hild\x12\r\n\x05value\x18\x01 \x01(\x02\"_\n\x03Map\x12)\n\x06values\x18\x01 \x03(\x0b\x32\x19.ord_test.Map.ValuesEntry\x1a-\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"\xa4\x01\n\tMapNested\x12\x33\n\x08\x63hildren\x18\x01 \x03(\x0b\x32!.ord_test.MapNested.ChildrenEntry\x1a\x16\n\x05\x43hild\x12\r\n\x05value\x18\x01 \x01(\x02\x1aJ\n\rChildrenEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.ord_test.MapNested.Child:\x02\x38\x01\x62\x06proto3'
)



_ENUM_ENUMVALUES = _descriptor.EnumDescriptor(
  name='EnumValues',
  full_name='ord_test.Enum.EnumValues',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECOND', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=241,
  serialized_end=293,
)
_sym_db.RegisterEnumDescriptor(_ENUM_ENUMVALUES)

_REPEATEDENUM_ENUMVALUES = _descriptor.EnumDescriptor(
  name='EnumValues',
  full_name='ord_test.RepeatedEnum.EnumValues',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SECOND', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=241,
  serialized_end=293,
)
_sym_db.RegisterEnumDescriptor(_REPEATEDENUM_ENUMVALUES)


_SCALAR = _descriptor.Descriptor(
  name='Scalar',
  full_name='ord_test.Scalar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int32_value', full_name='ord_test.Scalar.int32_value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int64_value', full_name='ord_test.Scalar.int64_value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='ord_test.Scalar.float_value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='ord_test.Scalar.string_value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_value', full_name='ord_test.Scalar.bytes_value', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=41,
  serialized_end=155,
)


_REPEATEDSCALAR = _descriptor.Descriptor(
  name='RepeatedScalar',
  full_name='ord_test.RepeatedScalar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='ord_test.RepeatedScalar.values', index=0,
      number=1, type=2, cpp_type=6, label=3,
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
  serialized_start=157,
  serialized_end=189,
)


_ENUM = _descriptor.Descriptor(
  name='Enum',
  full_name='ord_test.Enum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='ord_test.Enum.value', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ENUM_ENUMVALUES,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=293,
)


_REPEATEDENUM = _descriptor.Descriptor(
  name='RepeatedEnum',
  full_name='ord_test.RepeatedEnum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='ord_test.RepeatedEnum.values', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REPEATEDENUM_ENUMVALUES,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=414,
)


_NESTED_CHILD = _descriptor.Descriptor(
  name='Child',
  full_name='ord_test.Nested.Child',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='ord_test.Nested.Child.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=465,
  serialized_end=487,
)

_NESTED = _descriptor.Descriptor(
  name='Nested',
  full_name='ord_test.Nested',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='child', full_name='ord_test.Nested.child', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NESTED_CHILD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=416,
  serialized_end=487,
)


_REPEATEDNESTED_CHILD = _descriptor.Descriptor(
  name='Child',
  full_name='ord_test.RepeatedNested.Child',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='ord_test.RepeatedNested.Child.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=465,
  serialized_end=487,
)

_REPEATEDNESTED = _descriptor.Descriptor(
  name='RepeatedNested',
  full_name='ord_test.RepeatedNested',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='children', full_name='ord_test.RepeatedNested.children', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REPEATEDNESTED_CHILD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=489,
  serialized_end=579,
)


_MAP_VALUESENTRY = _descriptor.Descriptor(
  name='ValuesEntry',
  full_name='ord_test.Map.ValuesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ord_test.Map.ValuesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ord_test.Map.ValuesEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=631,
  serialized_end=676,
)

_MAP = _descriptor.Descriptor(
  name='Map',
  full_name='ord_test.Map',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='ord_test.Map.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MAP_VALUESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=581,
  serialized_end=676,
)


_MAPNESTED_CHILD = _descriptor.Descriptor(
  name='Child',
  full_name='ord_test.MapNested.Child',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='ord_test.MapNested.Child.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=465,
  serialized_end=487,
)

_MAPNESTED_CHILDRENENTRY = _descriptor.Descriptor(
  name='ChildrenEntry',
  full_name='ord_test.MapNested.ChildrenEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ord_test.MapNested.ChildrenEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ord_test.MapNested.ChildrenEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=769,
  serialized_end=843,
)

_MAPNESTED = _descriptor.Descriptor(
  name='MapNested',
  full_name='ord_test.MapNested',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='children', full_name='ord_test.MapNested.children', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MAPNESTED_CHILD, _MAPNESTED_CHILDRENENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=679,
  serialized_end=843,
)

_ENUM.fields_by_name['value'].enum_type = _ENUM_ENUMVALUES
_ENUM_ENUMVALUES.containing_type = _ENUM
_REPEATEDENUM.fields_by_name['values'].enum_type = _REPEATEDENUM_ENUMVALUES
_REPEATEDENUM_ENUMVALUES.containing_type = _REPEATEDENUM
_NESTED_CHILD.containing_type = _NESTED
_NESTED.fields_by_name['child'].message_type = _NESTED_CHILD
_REPEATEDNESTED_CHILD.containing_type = _REPEATEDNESTED
_REPEATEDNESTED.fields_by_name['children'].message_type = _REPEATEDNESTED_CHILD
_MAP_VALUESENTRY.containing_type = _MAP
_MAP.fields_by_name['values'].message_type = _MAP_VALUESENTRY
_MAPNESTED_CHILD.containing_type = _MAPNESTED
_MAPNESTED_CHILDRENENTRY.fields_by_name['value'].message_type = _MAPNESTED_CHILD
_MAPNESTED_CHILDRENENTRY.containing_type = _MAPNESTED
_MAPNESTED.fields_by_name['children'].message_type = _MAPNESTED_CHILDRENENTRY
DESCRIPTOR.message_types_by_name['Scalar'] = _SCALAR
DESCRIPTOR.message_types_by_name['RepeatedScalar'] = _REPEATEDSCALAR
DESCRIPTOR.message_types_by_name['Enum'] = _ENUM
DESCRIPTOR.message_types_by_name['RepeatedEnum'] = _REPEATEDENUM
DESCRIPTOR.message_types_by_name['Nested'] = _NESTED
DESCRIPTOR.message_types_by_name['RepeatedNested'] = _REPEATEDNESTED
DESCRIPTOR.message_types_by_name['Map'] = _MAP
DESCRIPTOR.message_types_by_name['MapNested'] = _MAPNESTED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Scalar = _reflection.GeneratedProtocolMessageType('Scalar', (_message.Message,), {
  'DESCRIPTOR' : _SCALAR,
  '__module__' : 'ord_schema.proto.test_pb2'
  # @@protoc_insertion_point(class_scope:ord_test.Scalar)
  })
_sym_db.RegisterMessage(Scalar)

RepeatedScalar = _reflection.GeneratedProtocolMessageType('RepeatedScalar', (_message.Message,), {
  'DESCRIPTOR' : _REPEATEDSCALAR,
  '__module__' : 'ord_schema.proto.test_pb2'
  # @@protoc_insertion_point(class_scope:ord_test.RepeatedScalar)
  })
_sym_db.RegisterMessage(RepeatedScalar)

Enum = _reflection.GeneratedProtocolMessageType('Enum', (_message.Message,), {
  'DESCRIPTOR' : _ENUM,
  '__module__' : 'ord_schema.proto.test_pb2'
  # @@protoc_insertion_point(class_scope:ord_test.Enum)
  })
_sym_db.RegisterMessage(Enum)

RepeatedEnum = _reflection.GeneratedProtocolMessageType('RepeatedEnum', (_message.Message,), {
  'DESCRIPTOR' : _REPEATEDENUM,
  '__module__' : 'ord_schema.proto.test_pb2'
  # @@protoc_insertion_point(class_scope:ord_test.RepeatedEnum)
  })
_sym_db.RegisterMessage(RepeatedEnum)

Nested = _reflection.GeneratedProtocolMessageType('Nested', (_message.Message,), {

  'Child' : _reflection.GeneratedProtocolMessageType('Child', (_message.Message,), {
    'DESCRIPTOR' : _NESTED_CHILD,
    '__module__' : 'ord_schema.proto.test_pb2'
    # @@protoc_insertion_point(class_scope:ord_test.Nested.Child)
    })
  ,
  'DESCRIPTOR' : _NESTED,
  '__module__' : 'ord_schema.proto.test_pb2'
  # @@protoc_insertion_point(class_scope:ord_test.Nested)
  })
_sym_db.RegisterMessage(Nested)
_sym_db.RegisterMessage(Nested.Child)

RepeatedNested = _reflection.GeneratedProtocolMessageType('RepeatedNested', (_message.Message,), {

  'Child' : _reflection.GeneratedProtocolMessageType('Child', (_message.Message,), {
    'DESCRIPTOR' : _REPEATEDNESTED_CHILD,
    '__module__' : 'ord_schema.proto.test_pb2'
    # @@protoc_insertion_point(class_scope:ord_test.RepeatedNested.Child)
    })
  ,
  'DESCRIPTOR' : _REPEATEDNESTED,
  '__module__' : 'ord_schema.proto.test_pb2'
  # @@protoc_insertion_point(class_scope:ord_test.RepeatedNested)
  })
_sym_db.RegisterMessage(RepeatedNested)
_sym_db.RegisterMessage(RepeatedNested.Child)

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), {

  'ValuesEntry' : _reflection.GeneratedProtocolMessageType('ValuesEntry', (_message.Message,), {
    'DESCRIPTOR' : _MAP_VALUESENTRY,
    '__module__' : 'ord_schema.proto.test_pb2'
    # @@protoc_insertion_point(class_scope:ord_test.Map.ValuesEntry)
    })
  ,
  'DESCRIPTOR' : _MAP,
  '__module__' : 'ord_schema.proto.test_pb2'
  # @@protoc_insertion_point(class_scope:ord_test.Map)
  })
_sym_db.RegisterMessage(Map)
_sym_db.RegisterMessage(Map.ValuesEntry)

MapNested = _reflection.GeneratedProtocolMessageType('MapNested', (_message.Message,), {

  'Child' : _reflection.GeneratedProtocolMessageType('Child', (_message.Message,), {
    'DESCRIPTOR' : _MAPNESTED_CHILD,
    '__module__' : 'ord_schema.proto.test_pb2'
    # @@protoc_insertion_point(class_scope:ord_test.MapNested.Child)
    })
  ,

  'ChildrenEntry' : _reflection.GeneratedProtocolMessageType('ChildrenEntry', (_message.Message,), {
    'DESCRIPTOR' : _MAPNESTED_CHILDRENENTRY,
    '__module__' : 'ord_schema.proto.test_pb2'
    # @@protoc_insertion_point(class_scope:ord_test.MapNested.ChildrenEntry)
    })
  ,
  'DESCRIPTOR' : _MAPNESTED,
  '__module__' : 'ord_schema.proto.test_pb2'
  # @@protoc_insertion_point(class_scope:ord_test.MapNested)
  })
_sym_db.RegisterMessage(MapNested)
_sym_db.RegisterMessage(MapNested.Child)
_sym_db.RegisterMessage(MapNested.ChildrenEntry)


_MAP_VALUESENTRY._options = None
_MAPNESTED_CHILDRENENTRY._options = None
# @@protoc_insertion_point(module_scope)
