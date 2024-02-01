from abc import ABC, abstractmethod


class TestClass(ABC):
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    @abstractmethod
    def name(self) -> str:
        return self._name
