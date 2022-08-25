import logging

from typing import (
    Any,
    Callable,
    Dict,
    List,
    Type,
)

from energomera.system import BaseFilter, ByteFilter, BaseProtocol

_LOGGER = logging.getLogger(__name__)


class Manager:
    def __init__(self, protocol: BaseProtocol):
        self._handlers: Dict[BaseFilter, List[Callable[..., Any]]] = {}
        self._protocol = protocol
        self._protocol.registry_handler(fn=self._process)

    @property
    def handlers(self) -> Dict[BaseFilter, List[Callable[..., Any]]]:
        return self._handlers

    @property
    def protocol(self) -> BaseProtocol:
        return self._protocol

    def registry_handler(self, fn: Callable[..., Any], filter_type: Type[BaseFilter] = ByteFilter, **kwargs) -> None:
        if not isinstance(filter_type, type(BaseFilter)):
            raise TypeError(f'{filter_type} is not a function \'BaseFilter\'')
        filter = filter_type(**kwargs)  # noqa
        if filter in self._handlers:
            self._handlers[filter].append(fn)
        else:
            self._handlers[filter] = [fn]

    def handler(self, **kwargs) -> Callable[..., Any]:
        def decorator(fn: Callable[..., Any]):
            self.registry_handler(fn=fn, **kwargs)
            return fn

        return decorator

    def _process(self, data: Any):
        for filter, handlers in self._handlers.items():
            if filter.check(data=data):
                for handler in handlers:
                    handler(key=filter.key, data=filter.extract_data(data))
