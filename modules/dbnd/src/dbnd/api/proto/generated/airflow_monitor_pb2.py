# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: airflow_monitor.proto
"""Generated protocol buffer code."""
from google.protobuf import (
    descriptor as _descriptor,
    message as _message,
    reflection as _reflection,
    symbol_database as _symbol_database,
    timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2,
)


# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="airflow_monitor.proto",
    package="dbnd.services.airflow_monitor",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x15\x61irflow_monitor.proto\x12\x1d\x64\x62nd.services.airflow_monitor\x1a\x1fgoogle/protobuf/timestamp.proto"\x99\x07\n\x11\x41irflowServerInfo\x12\x10\n\x08\x62\x61se_url\x18\x01 \x01(\t\x12\x1c\n\x0f\x61irflow_version\x18\x02 \x01(\tH\x00\x88\x01\x01\x12#\n\x16\x61irflow_export_version\x18\x03 \x01(\tH\x01\x88\x01\x01\x12$\n\x17\x61irflow_monitor_version\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x16\n\tdags_path\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x16\n\tlogs_path\x18\x06 \x01(\tH\x04\x88\x01\x01\x12\x37\n\x0elast_sync_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x05\x88\x01\x01\x12\x1b\n\x0emonitor_status\x18\x08 \x01(\tH\x06\x88\x01\x01\x12"\n\x15monitor_error_message\x18\t \x01(\tH\x07\x88\x01\x01\x12;\n\x12monitor_start_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x08\x88\x01\x01\x12\x34\n\x0bsynced_from\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampH\t\x88\x01\x01\x12\x32\n\tsynced_to\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.TimestampH\n\x88\x01\x01\x12\x15\n\x08\x61pi_mode\x18\r \x01(\tH\x0b\x88\x01\x01\x12\x1a\n\rsync_interval\x18\x0e \x01(\rH\x0c\x88\x01\x01\x12\x1c\n\x0fis_sync_enabled\x18\x0f \x01(\x08H\r\x88\x01\x01\x12\x14\n\x07\x66\x65tcher\x18\x10 \x01(\tH\x0e\x88\x01\x01\x12\x1f\n\x12\x63omposer_client_id\x18\x11 \x01(\tH\x0f\x88\x01\x01\x42\x12\n\x10_airflow_versionB\x19\n\x17_airflow_export_versionB\x1a\n\x18_airflow_monitor_versionB\x0c\n\n_dags_pathB\x0c\n\n_logs_pathB\x11\n\x0f_last_sync_timeB\x11\n\x0f_monitor_statusB\x18\n\x16_monitor_error_messageB\x15\n\x13_monitor_start_timeB\x0e\n\x0c_synced_fromB\x0c\n\n_synced_toB\x0b\n\t_api_modeB\x10\n\x0e_sync_intervalB\x12\n\x10_is_sync_enabledB\n\n\x08_fetcherB\x15\n\x13_composer_client_id"\x83\x01\n\x1cPostAirflowServerInfoRequest\x12M\n\x13\x61irflow_server_info\x18\x01 \x01(\x0b\x32\x30.dbnd.services.airflow_monitor.AirflowServerInfo\x12\x14\n\x0c\x65xternal_url\x18\x02 \x01(\t"\x1f\n\x1dPostAirflowServerInfoResponse2\xac\x01\n\x15\x41irflowMonitorService\x12\x92\x01\n\x15PostAirflowServerInfo\x12;.dbnd.services.airflow_monitor.PostAirflowServerInfoRequest\x1a<.dbnd.services.airflow_monitor.PostAirflowServerInfoResponseb\x06proto3',
    dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR],
)


_AIRFLOWSERVERINFO = _descriptor.Descriptor(
    name="AirflowServerInfo",
    full_name="dbnd.services.airflow_monitor.AirflowServerInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="base_url",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.base_url",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="airflow_version",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.airflow_version",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="airflow_export_version",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.airflow_export_version",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="airflow_monitor_version",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.airflow_monitor_version",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="dags_path",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.dags_path",
            index=4,
            number=5,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="logs_path",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.logs_path",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="last_sync_time",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.last_sync_time",
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="monitor_status",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.monitor_status",
            index=7,
            number=8,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="monitor_error_message",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.monitor_error_message",
            index=8,
            number=9,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="monitor_start_time",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.monitor_start_time",
            index=9,
            number=10,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="synced_from",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.synced_from",
            index=10,
            number=11,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="synced_to",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.synced_to",
            index=11,
            number=12,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="api_mode",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.api_mode",
            index=12,
            number=13,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="sync_interval",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.sync_interval",
            index=13,
            number=14,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="is_sync_enabled",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.is_sync_enabled",
            index=14,
            number=15,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="fetcher",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.fetcher",
            index=15,
            number=16,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="composer_client_id",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo.composer_client_id",
            index=16,
            number=17,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="_airflow_version",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._airflow_version",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_airflow_export_version",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._airflow_export_version",
            index=1,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_airflow_monitor_version",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._airflow_monitor_version",
            index=2,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_dags_path",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._dags_path",
            index=3,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_logs_path",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._logs_path",
            index=4,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_last_sync_time",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._last_sync_time",
            index=5,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_monitor_status",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._monitor_status",
            index=6,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_monitor_error_message",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._monitor_error_message",
            index=7,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_monitor_start_time",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._monitor_start_time",
            index=8,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_synced_from",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._synced_from",
            index=9,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_synced_to",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._synced_to",
            index=10,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_api_mode",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._api_mode",
            index=11,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_sync_interval",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._sync_interval",
            index=12,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_is_sync_enabled",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._is_sync_enabled",
            index=13,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_fetcher",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._fetcher",
            index=14,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
        _descriptor.OneofDescriptor(
            name="_composer_client_id",
            full_name="dbnd.services.airflow_monitor.AirflowServerInfo._composer_client_id",
            index=15,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=90,
    serialized_end=1011,
)


_POSTAIRFLOWSERVERINFOREQUEST = _descriptor.Descriptor(
    name="PostAirflowServerInfoRequest",
    full_name="dbnd.services.airflow_monitor.PostAirflowServerInfoRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="airflow_server_info",
            full_name="dbnd.services.airflow_monitor.PostAirflowServerInfoRequest.airflow_server_info",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="external_url",
            full_name="dbnd.services.airflow_monitor.PostAirflowServerInfoRequest.external_url",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1014,
    serialized_end=1145,
)


_POSTAIRFLOWSERVERINFORESPONSE = _descriptor.Descriptor(
    name="PostAirflowServerInfoResponse",
    full_name="dbnd.services.airflow_monitor.PostAirflowServerInfoResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1147,
    serialized_end=1178,
)

_AIRFLOWSERVERINFO.fields_by_name[
    "last_sync_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_AIRFLOWSERVERINFO.fields_by_name[
    "monitor_start_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_AIRFLOWSERVERINFO.fields_by_name[
    "synced_from"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_AIRFLOWSERVERINFO.fields_by_name[
    "synced_to"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_AIRFLOWSERVERINFO.oneofs_by_name["_airflow_version"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["airflow_version"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "airflow_version"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_airflow_version"]
_AIRFLOWSERVERINFO.oneofs_by_name["_airflow_export_version"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["airflow_export_version"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "airflow_export_version"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_airflow_export_version"]
_AIRFLOWSERVERINFO.oneofs_by_name["_airflow_monitor_version"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["airflow_monitor_version"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "airflow_monitor_version"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_airflow_monitor_version"]
_AIRFLOWSERVERINFO.oneofs_by_name["_dags_path"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["dags_path"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "dags_path"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_dags_path"]
_AIRFLOWSERVERINFO.oneofs_by_name["_logs_path"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["logs_path"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "logs_path"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_logs_path"]
_AIRFLOWSERVERINFO.oneofs_by_name["_last_sync_time"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["last_sync_time"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "last_sync_time"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_last_sync_time"]
_AIRFLOWSERVERINFO.oneofs_by_name["_monitor_status"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["monitor_status"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "monitor_status"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_monitor_status"]
_AIRFLOWSERVERINFO.oneofs_by_name["_monitor_error_message"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["monitor_error_message"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "monitor_error_message"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_monitor_error_message"]
_AIRFLOWSERVERINFO.oneofs_by_name["_monitor_start_time"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["monitor_start_time"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "monitor_start_time"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_monitor_start_time"]
_AIRFLOWSERVERINFO.oneofs_by_name["_synced_from"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["synced_from"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "synced_from"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_synced_from"]
_AIRFLOWSERVERINFO.oneofs_by_name["_synced_to"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["synced_to"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "synced_to"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_synced_to"]
_AIRFLOWSERVERINFO.oneofs_by_name["_api_mode"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["api_mode"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "api_mode"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_api_mode"]
_AIRFLOWSERVERINFO.oneofs_by_name["_sync_interval"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["sync_interval"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "sync_interval"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_sync_interval"]
_AIRFLOWSERVERINFO.oneofs_by_name["_is_sync_enabled"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["is_sync_enabled"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "is_sync_enabled"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_is_sync_enabled"]
_AIRFLOWSERVERINFO.oneofs_by_name["_fetcher"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["fetcher"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "fetcher"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_fetcher"]
_AIRFLOWSERVERINFO.oneofs_by_name["_composer_client_id"].fields.append(
    _AIRFLOWSERVERINFO.fields_by_name["composer_client_id"]
)
_AIRFLOWSERVERINFO.fields_by_name[
    "composer_client_id"
].containing_oneof = _AIRFLOWSERVERINFO.oneofs_by_name["_composer_client_id"]
_POSTAIRFLOWSERVERINFOREQUEST.fields_by_name[
    "airflow_server_info"
].message_type = _AIRFLOWSERVERINFO
DESCRIPTOR.message_types_by_name["AirflowServerInfo"] = _AIRFLOWSERVERINFO
DESCRIPTOR.message_types_by_name[
    "PostAirflowServerInfoRequest"
] = _POSTAIRFLOWSERVERINFOREQUEST
DESCRIPTOR.message_types_by_name[
    "PostAirflowServerInfoResponse"
] = _POSTAIRFLOWSERVERINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AirflowServerInfo = _reflection.GeneratedProtocolMessageType(
    "AirflowServerInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _AIRFLOWSERVERINFO,
        "__module__": "airflow_monitor_pb2"
        # @@protoc_insertion_point(class_scope:dbnd.services.airflow_monitor.AirflowServerInfo)
    },
)
_sym_db.RegisterMessage(AirflowServerInfo)

PostAirflowServerInfoRequest = _reflection.GeneratedProtocolMessageType(
    "PostAirflowServerInfoRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _POSTAIRFLOWSERVERINFOREQUEST,
        "__module__": "airflow_monitor_pb2"
        # @@protoc_insertion_point(class_scope:dbnd.services.airflow_monitor.PostAirflowServerInfoRequest)
    },
)
_sym_db.RegisterMessage(PostAirflowServerInfoRequest)

PostAirflowServerInfoResponse = _reflection.GeneratedProtocolMessageType(
    "PostAirflowServerInfoResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _POSTAIRFLOWSERVERINFORESPONSE,
        "__module__": "airflow_monitor_pb2"
        # @@protoc_insertion_point(class_scope:dbnd.services.airflow_monitor.PostAirflowServerInfoResponse)
    },
)
_sym_db.RegisterMessage(PostAirflowServerInfoResponse)


_AIRFLOWMONITORSERVICE = _descriptor.ServiceDescriptor(
    name="AirflowMonitorService",
    full_name="dbnd.services.airflow_monitor.AirflowMonitorService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=1181,
    serialized_end=1353,
    methods=[
        _descriptor.MethodDescriptor(
            name="PostAirflowServerInfo",
            full_name="dbnd.services.airflow_monitor.AirflowMonitorService.PostAirflowServerInfo",
            index=0,
            containing_service=None,
            input_type=_POSTAIRFLOWSERVERINFOREQUEST,
            output_type=_POSTAIRFLOWSERVERINFORESPONSE,
            serialized_options=None,
            create_key=_descriptor._internal_create_key,
        )
    ],
)
_sym_db.RegisterServiceDescriptor(_AIRFLOWMONITORSERVICE)

DESCRIPTOR.services_by_name["AirflowMonitorService"] = _AIRFLOWMONITORSERVICE

# @@protoc_insertion_point(module_scope)
