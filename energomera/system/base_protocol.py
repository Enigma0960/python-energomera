from typing import (
    Any,
    Callable,
    List,
)


class BaseProtocol:
    def __init__(self):
        self._handlers: List[Callable[..., Any]] = []

    @property
    def handlers(self) -> List[Callable[..., Any]]:
        return self._handlers

    def registry_handler(self, fn=Callable[..., Any]):
        self._handlers.append(fn)

    def handler(self) -> Callable[..., Any]:
        def decorator(fn: Callable[..., Any]):
            self.registry_handler(fn=fn)
            return fn

        return decorator
