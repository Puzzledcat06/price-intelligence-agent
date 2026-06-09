from abc import ABC, abstractmethod


class BaseConnector(ABC):

    @abstractmethod
    async def search_product(self, query: str):
        pass