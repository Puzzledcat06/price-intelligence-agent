import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import asyncio

from services.connector_manager import ConnectorManager
from services.price_analyzer import PriceAnalyzer


async def main():

    manager = ConnectorManager()

    products = await manager.search_product(
        "iphone 17 pro"
    )

    cheapest = PriceAnalyzer.get_lowest_price(
        products
    )

    print(cheapest)


asyncio.run(main())