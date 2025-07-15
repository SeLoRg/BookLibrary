from abc import ABC, abstractmethod
from typing import Any, Optional, Dict
import httpx
from logging import Logger


class BaseApiClient(ABC):
    def __init__(
        self,
        base_url: str,
        logger: Logger,
        timeout: float = 10.0,
    ):
        self.base_url = base_url
        self.timeout = timeout
        self.client = httpx.AsyncClient(timeout=self.timeout)
        self.logger = logger

    async def _request(self, method: str, url: str, **kwargs) -> Optional[dict, Any]:
        try:
            full_url = self.base_url + url
            self.logger.debug(
                f"Sending {method.upper()} request to {full_url} with {kwargs=}"
            )
            response = await self.client.request(method, full_url, **kwargs)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            self.logger.error(f"HTTP error during request to {url}: {str(e)}")
            raise

    @abstractmethod
    async def send_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Any: ...

    async def close(self):
        await self.client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
