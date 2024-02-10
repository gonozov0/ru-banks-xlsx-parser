from abc import ABC, abstractmethod

from src import dto


class IBank(ABC):
    @abstractmethod
    async def get_operations(self) -> dto.Operations:
        pass

    @abstractmethod
    async def get_name(self) -> str:
        pass
