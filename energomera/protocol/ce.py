from attr import attrs, attrib
from typing import List, Tuple, Optional

_MIN_SIZE = 10
_WAKE_CRC = 0xB5

_WAKE_TAG_FEND = 0xC0
_WAKE_TAG_FESC = 0xDB
_WAKE_TAG_TFEND = 0xDC
_WAKE_TAG_TFESC = 0xDD

_CE_OPT_MODE = 0x48


def _calc_crc(data: bytes) -> bytes:
    return b''


def _get_data(data: bytes, size: int = 1) -> Tuple[bytes, bytes]:
    pass


def _extract_packet(data: bytes) -> Optional['Packet']:
    if len(data) < _MIN_SIZE:
        return None

    if data[0] != _CE_OPT_MODE:
        return None

    direction, data = _get_data(data, 1)
    sender, data = _get_data(data, 1)

    return Packet(direction=direction, sender=sender)


@attrs(slots=True, repr=False)
class Packet:
    direction = attrib(type=int)
    sender = attrib(type=int)

    _input_buffer: bytes = b''

    def from_dict(self):
        pass

    def to_dict(self):
        pass

    @classmethod
    def process(cls, data: bytes) -> List['Packet']:
        if len(data) == 0:
            return []
        cls._input_buffer += data

        result: List[Packet] = []
        while len(cls._input_buffer) > _MIN_SIZE:
            input_data = cls._input_buffer.split(_WAKE_TAG_FEND.to_bytes(length=1, byteorder="big"))
            if len(input_data) == 0:
                break

            candidates = input_data[:-1]
            perspective = input_data[-1]

            result = [packet for packet in [_extract_packet(candidate) for candidate in candidates] if
                      packet is not None]

            packet = _extract_packet(perspective)
            if packet is not None:
                result.append(packet)
                perspective = b''

            cls._input_buffer = perspective

        return result
