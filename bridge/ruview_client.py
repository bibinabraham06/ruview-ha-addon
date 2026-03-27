import aiohttp
from bridge.models import ZoneData


class RuViewClient:
    def __init__(self, base_url: str):
        self._base_url = base_url.rstrip("/")

    async def fetch_zones(self) -> list[ZoneData]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self._base_url}/api/v1/sensing/latest",
                timeout=aiohttp.ClientTimeout(total=5),
            ) as resp:
                resp.raise_for_status()
                data = await resp.json()
                return [ZoneData(**z) for z in data.get("zones", [])]

    async def is_healthy(self) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"{self._base_url}/health",
                    timeout=aiohttp.ClientTimeout(total=3),
                ) as resp:
                    return resp.status == 200
        except Exception:
            return False
