import abc, typing

class My_Maps_interface(abc.ABC):

    @abc.abstractmethod
    def __fullscreen__(self: typing.Self, configure: str | None = None) -> None:
        pass
