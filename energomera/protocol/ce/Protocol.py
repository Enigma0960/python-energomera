import logging

from energomera.interface.interface import AbstractInterface

_LOGGER = logging.getLogger(__name__)


class Protocol:

    def __init__(self, transport: AbstractInterface):
        self._transport = transport
