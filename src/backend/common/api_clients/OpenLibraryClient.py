from typing import Optional, Dict, Any
from src.backend.common.api_clients.BaseApiClient import BaseApiClient


class OpenLibraryClient(BaseApiClient):
    async def send_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Optional[Dict[str, Any]]:
        return await self._request(
            method, endpoint, params=params, headers=headers, json=json
        )

    async def search_book_info(self, title: str) -> Optional[Dict[str, Any]]:
        search_data = await self.send_request(
            method="GET", endpoint="/search.json", params={"title": title}
        )
        if not search_data["docs"]:
            return None

        first = search_data["docs"][0]
        work_key = first.get("key")  # /works/OL...
        cover_id = first.get("cover_i")
        author = first.get("author_name", [""])[0]
        title = first.get("title", "")
        year = first.get("first_publish_year", "")

        # 2. Получение описания и рейтинга
        work_data = await self.send_request(method="GET", endpoint=f"{work_key}.json")

        description = None
        if isinstance(work_data.get("description"), dict):
            description = work_data["description"].get("value")
        elif isinstance(work_data.get("description"), str):
            description = work_data["description"]

        # 3. Получение рейтинга
        rating_data = await self.send_request(
            method="GET", endpoint=f"{work_key}/ratings.json"
        )
        rating_data.get("summary", {}).get("average", 0.0)
        rating = None

        if isinstance(rating_data.get("summary"), dict):
            description = rating_data.get("summary", {}).get("average", 0.0)

        # 4. Сбор результата
        return {
            "title": title,
            "author": author,
            "year": year,
            "cover_url": (
                f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
                if cover_id
                else None
            ),
            "description": description,
            "rating": rating,
        }
