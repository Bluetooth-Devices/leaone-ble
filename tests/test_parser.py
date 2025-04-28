from uuid import UUID

from bleak.backends.device import BLEDevice
from bluetooth_data_tools import monotonic_time_coarse
from bluetooth_sensor_state_data import SensorUpdate
from habluetooth import BluetoothServiceInfoBleak
from sensor_state_data import (
    DeviceKey,
    SensorDescription,
    SensorDeviceClass,
    SensorDeviceInfo,
    SensorValue,
    Units,
)

from leaone_ble.parser import LeaoneBluetoothDeviceData


def make_bluetooth_service_info(
    name: str,
    manufacturer_data: dict[int, bytes],
    service_uuids: list[str],
    address: str,
    rssi: int,
    service_data: dict[UUID, bytes],
    source: str,
    tx_power: int = 0,
    raw: bytes | None = None,
) -> BluetoothServiceInfoBleak:
    return BluetoothServiceInfoBleak(
        name=name,
        manufacturer_data=manufacturer_data,
        service_uuids=service_uuids,
        address=address,
        rssi=rssi,
        service_data=service_data,
        source=source,
        device=BLEDevice(
            name=name,
            address=address,
            details={},
            rssi=rssi,
        ),
        time=monotonic_time_coarse(),
        advertisement=None,
        connectable=True,
        tx_power=tx_power,
        raw=raw,
    )


SCALE_SERVICE_INFO = make_bluetooth_service_info(
    name="",
    address="5F:5A:5C:52:D3:94",
    rssi=-63,
    manufacturer_data={57280: b"\x06\xa4\x00\x00\x00\x020_Z\\R\xd3\x94"},
    service_uuids=[],
    service_data={},
    source="local",
)

SCALE_SERVICE_INFO_RAW = make_bluetooth_service_info(
    name="",
    address="5F:5A:5C:52:D3:94",
    rssi=-63,
    manufacturer_data={63424: b"\x06\xa4\x13\x80\x00\x021_Z\\R\xd3\x94"},
    service_uuids=[],
    service_data={},
    source="local",
    raw=b"\x10\xff\x00\xdf\x06\xa4\x00\x00\x00\x020_Z\\R\xd3\x94",
)
SCALE_SERVICE_INFO_2 = make_bluetooth_service_info(
    name="",
    address="5F:5A:5C:52:D3:94",
    rssi=-63,
    manufacturer_data={
        57280: b"\x06\xa4\x00\x00\x00\x020_Z\\R\xd3\x94",
        63424: b"\x06\xa4\x13\x80\x00\x021_Z\\R\xd3\x94",
    },
    service_uuids=[],
    service_data={},
    source="local",
)
SCALE_SERVICE_INFO_3 = make_bluetooth_service_info(
    name="",
    address="5F:5A:5C:52:D3:94",
    rssi=-63,
    manufacturer_data={
        57280: b"\x06\xa4\x00\x00\x00\x020_Z\\R\xd3\x94",
        63424: b"\x06\xa4\x13\x80\x00\x021_Z\\R\xd3\x94",
        6592: b"\x06\x8e\x00\x00\x00\x020_Z\\R\xd3\x94",
    },
    service_uuids=[],
    service_data={},
    source="local",
)

SCALE_SERVICE_INFO_KGS = make_bluetooth_service_info(
    name="",
    address="5F:5A:5C:52:D3:94",
    rssi=-63,
    manufacturer_data={22976: b"\x00\x00\x00\x00\x00\x02 _Z\\R\xd3\x94"},
    service_uuids=[],
    service_data={},
    source="local",
)

SCALE_SERVICE_INFO_KGS_2 = make_bluetooth_service_info(
    name="",
    address="5F:5A:5C:52:D3:94",
    rssi=-63,
    manufacturer_data={
        22976: b"\x00\x00\x00\x00\x00\x02 _Z\\R\xd3\x94",
        27328: b"\x00\x00\x00\x00\x00\x02 _Z\\R\xd3\x94",
    },
    service_uuids=[],
    service_data={},
    source="local",
)


def test_can_create():
    LeaoneBluetoothDeviceData()


def test_scale_lbs():
    parser = LeaoneBluetoothDeviceData()
    result = parser.update(SCALE_SERVICE_INFO)
    assert result == SensorUpdate(
        title="TZC4 D394",
        devices={
            None: SensorDeviceInfo(
                name="TZC4 D394",
                model="TZC4",
                manufacturer="Leaone",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorDescription(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                device_class=SensorDeviceClass.MASS_NON_STABILIZED,
                native_unit_of_measurement=Units.MASS_KILOGRAMS,
            ),
            DeviceKey(key="packet_id", device_id=None): SensorDescription(
                device_key=DeviceKey(key="packet_id", device_id=None),
                device_class=SensorDeviceClass.PACKET_ID,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorValue(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                name="Non " "Stabilized " "Mass",
                native_value=77.11,
            ),
            DeviceKey(key="packet_id", device_id=None): SensorValue(
                device_key=DeviceKey(key="packet_id", device_id=None),
                name="Packet " "Id",
                native_value=57136,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-63,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )
    result = parser.update(SCALE_SERVICE_INFO_2)
    assert result == SensorUpdate(
        title="TZC4 D394",
        devices={
            None: SensorDeviceInfo(
                name="TZC4 D394",
                model="TZC4",
                manufacturer="Leaone",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorDescription(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                device_class=SensorDeviceClass.MASS_NON_STABILIZED,
                native_unit_of_measurement=Units.MASS_KILOGRAMS,
            ),
            DeviceKey(key="packet_id", device_id=None): SensorDescription(
                device_key=DeviceKey(key="packet_id", device_id=None),
                device_class=SensorDeviceClass.PACKET_ID,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="mass", device_id=None): SensorDescription(
                device_key=DeviceKey(key="mass", device_id=None),
                device_class=SensorDeviceClass.MASS,
                native_unit_of_measurement=Units.MASS_KILOGRAMS,
            ),
            DeviceKey(key="impedance", device_id=None): SensorDescription(
                device_key=DeviceKey(key="impedance", device_id=None),
                device_class=SensorDeviceClass.IMPEDANCE,
                native_unit_of_measurement=Units.OHM,
            ),
        },
        entity_values={
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorValue(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                name="Non " "Stabilized " "Mass",
                native_value=77.11,
            ),
            DeviceKey(key="packet_id", device_id=None): SensorValue(
                device_key=DeviceKey(key="packet_id", device_id=None),
                name="Packet " "Id",
                native_value=63281,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-63,
            ),
            DeviceKey(key="mass", device_id=None): SensorValue(
                device_key=DeviceKey(key="mass", device_id=None),
                name="Mass",
                native_value=77.11,
            ),
            DeviceKey(key="impedance", device_id=None): SensorValue(
                device_key=DeviceKey(key="impedance", device_id=None),
                name="Impedance",
                native_value=499.2,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )

    service_info = SCALE_SERVICE_INFO_3
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title="TZC4 D394",
        devices={
            None: SensorDeviceInfo(
                name="TZC4 D394",
                model="TZC4",
                manufacturer="Leaone",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="packet_id", device_id=None): SensorDescription(
                device_key=DeviceKey(key="packet_id", device_id=None),
                device_class=SensorDeviceClass.PACKET_ID,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorDescription(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                device_class=SensorDeviceClass.MASS_NON_STABILIZED,
                native_unit_of_measurement=Units.MASS_KILOGRAMS,
            ),
            DeviceKey(key="impedance", device_id=None): SensorDescription(
                device_key=DeviceKey(key="impedance", device_id=None),
                device_class=SensorDeviceClass.IMPEDANCE,
                native_unit_of_measurement=Units.OHM,
            ),
            DeviceKey(key="mass", device_id=None): SensorDescription(
                device_key=DeviceKey(key="mass", device_id=None),
                device_class=SensorDeviceClass.MASS,
                native_unit_of_measurement=Units.MASS_KILOGRAMS,
            ),
        },
        entity_values={
            DeviceKey(key="packet_id", device_id=None): SensorValue(
                device_key=DeviceKey(key="packet_id", device_id=None),
                name="Packet " "Id",
                native_value=6448,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-63,
            ),
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorValue(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                name="Non " "Stabilized " "Mass",
                native_value=76.11,
            ),
            DeviceKey(key="impedance", device_id=None): SensorValue(
                device_key=DeviceKey(key="impedance", device_id=None),
                name="Impedance",
                native_value=499.2,
            ),
            DeviceKey(key="mass", device_id=None): SensorValue(
                device_key=DeviceKey(key="mass", device_id=None),
                name="Mass",
                native_value=77.11,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )


def test_scale_lbs_raw():
    parser = LeaoneBluetoothDeviceData()
    result = parser.update(SCALE_SERVICE_INFO_RAW)
    assert result == SensorUpdate(
        title="TZC4 D394",
        devices={
            None: SensorDeviceInfo(
                name="TZC4 D394",
                model="TZC4",
                manufacturer="Leaone",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorDescription(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                device_class=SensorDeviceClass.MASS_NON_STABILIZED,
                native_unit_of_measurement=Units.MASS_KILOGRAMS,
            ),
            DeviceKey(key="packet_id", device_id=None): SensorDescription(
                device_key=DeviceKey(key="packet_id", device_id=None),
                device_class=SensorDeviceClass.PACKET_ID,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorValue(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                name="Non " "Stabilized " "Mass",
                native_value=77.11,
            ),
            DeviceKey(key="packet_id", device_id=None): SensorValue(
                device_key=DeviceKey(key="packet_id", device_id=None),
                name="Packet " "Id",
                native_value=57136,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-63,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )


def test_scale_kgs():
    parser = LeaoneBluetoothDeviceData()
    result = parser.update(SCALE_SERVICE_INFO_KGS)
    assert result == SensorUpdate(
        title="TZC4 D394",
        devices={
            None: SensorDeviceInfo(
                name="TZC4 D394",
                model="TZC4",
                manufacturer="Leaone",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorDescription(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                device_class=SensorDeviceClass.MASS_NON_STABILIZED,
                native_unit_of_measurement=Units.MASS_KILOGRAMS,
            ),
            DeviceKey(key="packet_id", device_id=None): SensorDescription(
                device_key=DeviceKey(key="packet_id", device_id=None),
                device_class=SensorDeviceClass.PACKET_ID,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorValue(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                name="Non " "Stabilized " "Mass",
                native_value=0.0,
            ),
            DeviceKey(key="packet_id", device_id=None): SensorValue(
                device_key=DeviceKey(key="packet_id", device_id=None),
                name="Packet " "Id",
                native_value=22816,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-63,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )
    result = parser.update(SCALE_SERVICE_INFO_KGS_2)
    assert result == SensorUpdate(
        title="TZC4 D394",
        devices={
            None: SensorDeviceInfo(
                name="TZC4 D394",
                model="TZC4",
                manufacturer="Leaone",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorDescription(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                device_class=SensorDeviceClass.MASS_NON_STABILIZED,
                native_unit_of_measurement=Units.MASS_KILOGRAMS,
            ),
            DeviceKey(key="packet_id", device_id=None): SensorDescription(
                device_key=DeviceKey(key="packet_id", device_id=None),
                device_class=SensorDeviceClass.PACKET_ID,
                native_unit_of_measurement=None,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="non_stabilized_mass", device_id=None): SensorValue(
                device_key=DeviceKey(key="non_stabilized_mass", device_id=None),
                name="Non " "Stabilized " "Mass",
                native_value=0.0,
            ),
            DeviceKey(key="packet_id", device_id=None): SensorValue(
                device_key=DeviceKey(key="packet_id", device_id=None),
                name="Packet " "Id",
                native_value=27168,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-63,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
        events={},
    )
