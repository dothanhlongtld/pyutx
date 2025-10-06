from .api.async_support.clients import APIClient
from .types import TRADING_PLATFORM


def apyutx(trading_platform: TRADING_PLATFORM, config: dict = {}) -> APIClient:
    match trading_platform:
        case "okx":
            from .api.async_support.okx import OKXClient

            return OKXClient(config)
        case "binance_usdm":
            from .api.async_support.binance import BinanceUSDMClient

            return BinanceUSDMClient(config)
        case "bybit_linear_futures":
            from .api.async_support.bybit import BybitLinearFuturesClient

            return BybitLinearFuturesClient(config)
        case "bingx":
            from .api.async_support.bingx import BingXClient

            return BingXClient(config)
        case _:
            raise ValueError(f"Unsupported trading platform: {trading_platform}")
