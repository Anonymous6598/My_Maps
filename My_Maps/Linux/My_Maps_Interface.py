import abc, typing

class My_Maps_Interface(abc.ABC):

    @abc.abstractmethod
    def __search__(self: typing.Self) -> None:
        pass