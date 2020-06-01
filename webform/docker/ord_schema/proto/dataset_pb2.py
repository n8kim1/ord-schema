# Copyright 2020 The Open Reaction Database Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ord-schema/proto/dataset.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ord_schema.proto import reaction_pb2 as ord__schema_dot_proto_dot_reaction__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ord-schema/proto/dataset.proto',
  package='ord',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1eord-schema/proto/dataset.proto\x12\x03ord\x1a\x1ford-schema/proto/reaction.proto\"\x9f\x01\n\x07\x44\x61taset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12 \n\treactions\x18\x03 \x03(\x0b\x32\r.ord.Reaction\x12\x14\n\x0creaction_ids\x18\x04 \x03(\t\x12%\n\x08\x65xamples\x18\x05 \x03(\x0b\x32\x13.ord.DatasetExample\x12\x12\n\ndataset_id\x18\x06 \x01(\t\"U\n\x0e\x44\x61tasetExample\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12!\n\x07\x63reated\x18\x03 \x01(\x0b\x32\x10.ord.RecordEventb\x06proto3'
  ,
  dependencies=[ord__schema_dot_proto_dot_reaction__pb2.DESCRIPTOR,])




_DATASET = _descriptor.Descriptor(
  name='Dataset',
  full_name='ord.Dataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ord.Dataset.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ord.Dataset.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reactions', full_name='ord.Dataset.reactions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reaction_ids', full_name='ord.Dataset.reaction_ids', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='examples', full_name='ord.Dataset.examples', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ord.Dataset.dataset_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_end=232,
)


_DATASETEXAMPLE = _descriptor.Descriptor(
  name='DatasetExample',
  full_name='ord.DatasetExample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='description', full_name='ord.DatasetExample.description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='ord.DatasetExample.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created', full_name='ord.DatasetExample.created', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=234,
  serialized_end=319,
)

_DATASET.fields_by_name['reactions'].message_type = ord__schema_dot_proto_dot_reaction__pb2._REACTION
_DATASET.fields_by_name['examples'].message_type = _DATASETEXAMPLE
_DATASETEXAMPLE.fields_by_name['created'].message_type = ord__schema_dot_proto_dot_reaction__pb2._RECORDEVENT
DESCRIPTOR.message_types_by_name['Dataset'] = _DATASET
DESCRIPTOR.message_types_by_name['DatasetExample'] = _DATASETEXAMPLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), {
  'DESCRIPTOR' : _DATASET,
  '__module__' : 'ord_schema.proto.dataset_pb2'
  # @@protoc_insertion_point(class_scope:ord.Dataset)
  })
_sym_db.RegisterMessage(Dataset)

DatasetExample = _reflection.GeneratedProtocolMessageType('DatasetExample', (_message.Message,), {
  'DESCRIPTOR' : _DATASETEXAMPLE,
  '__module__' : 'ord_schema.proto.dataset_pb2'
  # @@protoc_insertion_point(class_scope:ord.DatasetExample)
  })
_sym_db.RegisterMessage(DatasetExample)


# @@protoc_insertion_point(module_scope)
