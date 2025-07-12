from abc import ABC, abstractmethod
from typing import Any
import httpx
import logging


class BaseApiClient(ABC):
    def __init__(self, base_url: str, timeout: float = 10.0):
        self.base_url = base_url
        self.timeout = timeout
        self.client = httpx.AsyncClient(timeout=self.timeout)
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    async def send_request(self, method: str, endpoint: str, **kwargs) -> Any: ...

    async def close(self):
        await self.client.aclose()
