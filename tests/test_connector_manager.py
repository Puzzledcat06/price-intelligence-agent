import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import asyncio

from services.connector_manager import ConnectorManager


async def main():

    manager = ConnectorManager()

    products = await manager.search_product(
        "iphone 17 pro"
    )

    for product in products:
        print(product)


asyncio.run(main())