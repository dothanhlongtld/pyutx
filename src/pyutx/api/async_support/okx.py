from httpx import AsyncClient

from ...errors import Error
from .clients import APIClient


class OKXClient(APIClient):
    def __init__(self, config: dict = {}):
        super().__init__(config)

        self.base_url = "https://www.okx.com"
        self.http_client = AsyncClient(
            base_url=self.base_url,
            headers={"x-simulated-trading": "1" if self.demo else "0"},
        )
        self.timeframe_mapping = {
            "1m": "1",
            "3m": "3",
            "5m": "5",
            "15m": "15",
            "30m": "30",
            "1h": "60",
            "2h": "120",
            "4h": "240",
            "6h": "360",
            "12h": "720",
            "1d": "D",
            "1w": "W",
            "1M": "M",
        }

    async def get_candles(self, symbol, timeframe, since=None, limit=100):
        mapped_timeframe = self.timeframe_mapping.get(timeframe, None)
        if mapped_timeframe is None:
            raise ValueError(f"Unsupported timeframe: {timeframe}")

        endpoint = "/api/v5/market/candles"
        params = {
            "instId": symbol,
            "bar": self.timeframe_mapping[timeframe],
            "limit": limit,
        }

        if since is not None:
            params["before"] = since

        response = await self.http_client.get(endpoint, params=params)
        response.raise_for_status()

        response_data = response.json()

        code = response_data.get("code")
        if code != "0":
            raise Error(int(code), response_data.get("msg", "Unknown error"))

        return [
            [
                int(candle[0]),  # timestamp
                float(candle[1]),  # open
                float(candle[2]),  # high
                float(candle[3]),  # low
                float(candle[4]),  # close
                float(candle[5]),  # volume
            ]
            for candle in response_data.get("data", [])[::-1]
        ]
