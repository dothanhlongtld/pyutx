import asyncio

from src.pyutx.api.async_support.factories import get_api_client


async def test_okx():
    okx = get_api_client("okx", demo=True)

    candles = await okx.get_candles("BTC-USDT-SWAP", "1h", limit=100)

    await okx.close()

    print(candles)
    print(len(candles))


async def test_binance_usdm():
    binance_usdm = get_api_client("binance_usdm", demo=True)

    candles = await binance_usdm.get_candles("BTCUSDT", "1h", limit=100)

    await binance_usdm.close()

    print(candles)
    print(len(candles))


async def test_bybit_linear_futures():
    bybit = get_api_client("bybit_linear_futures", demo=True)

    candles = await bybit.get_candles("BTCUSDT", "1h", limit=100)

    await bybit.close()

    print(candles)
    print(len(candles))


async def test_bingx():
    bingx = get_api_client("bingx", config={"demo": True})

    candles = await bingx.get_candles("BTC-USDT", "1h", limit=100, since=1759590000000)

    await bingx.close()

    print(candles)
    print(len(candles))


if __name__ == "__main__":
    asyncio.run(test_bingx())
