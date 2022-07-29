from enum import Enum
from attr import attrs, attrib
from typing import Optional, Any, Dict

BROADCAST_ADDRESS = 0xFFFF


class ClassAccess(Enum):
    ExecutionCommand = 0x05
    ErrorCommand = 0x07


class ErrorCode(Enum):
    CommandMissing = 0x00


class Command(Enum):
    Ping = 0x0001


@attrs(slots=True, repr=False)
class Packet:
    sender = attrib(type=int, default=0x0000)
    receiver = attrib(type=int, default=BROADCAST_ADDRESS)
    password = attrib(type=Optional[int], default=None)
    direct = attrib(type=bool, default=False)
    access = attrib(type=ClassAccess, default=ClassAccess.ExecutionCommand)
    error = attrib(type=Optional[ErrorCode], default=None)
    command = attrib(type=Command, default=Command.Ping)
    data = attrib(type=Optional[Any], default=None)
