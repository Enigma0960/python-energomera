import logging

from enum import Enum
from attr import attrs, attrib
from typing import Optional, Any, Dict

_LOGGER = logging.getLogger(__name__)

BROADCAST_ADDRESS = 0xFFFF
DEFAULT_PC_ADDRESS = 0x0


class Access(Enum):
    ExecutionCommand = 0x05
    ErrorCommand = 0x07


class ErrorCode(Enum):
    CommandMissing = 0x00
    InvalidPacketFormat = 0x01
    PermissionDenied = 0x02
    NotEnoughParameters = 0x03
    ConfigError = 0x04
    NotPressButton = 0x05
    ParametersError = 0x10
    MemoryWriteError = 0x20
    TariffError = 0x40
    ReadMemoryError = 0x80

    def __str__(self) -> str:
        # noinspection PyTypeChecker
        code: int = self.value

        messages: Dict[int, str] = {
            0x00: 'Команда отсутствует',
            0x01: 'Неверный формат принятого пакета',
            0x02: 'Недостаточный уровень доступа',
            0x03: 'Неверное количество параметров',
            0x04: 'Ошибка конфигурации',
            0x05: 'Не нажата кнопка \'Доступ\'',
            0x10: 'Не верный параметр',
            0x20: 'Неверная запись в память',
            0x40: 'Недопустимая тарифная программа',
            0x80: 'Ошибка чтения внешней памяти',
        }
        return f'<{type(self).__name__}.{self.name} {hex(code)}>: {messages[code]}'


class Command(Enum):
    Ping = 0x0001


@attrs(slots=True, repr=False)
class Packet:
    sender = attrib(type=int, default=0x0000)
    receiver = attrib(type=int, default=BROADCAST_ADDRESS)
    password = attrib(type=Optional[int], default=None)
    direct = attrib(type=bool, default=False)
    access = attrib(type=Access, default=Access.ExecutionCommand)
    error = attrib(type=Optional[ErrorCode], default=None)
    command = attrib(type=Command, default=Command.Ping)
    data = attrib(type=Optional[Any], default=None)
