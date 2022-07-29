class AbstractInterface:
    def write(self, data: bytes) -> None:
        raise NotImplementedError

    def read(self) -> bytes:
        raise NotImplementedError
