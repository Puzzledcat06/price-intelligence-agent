import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import asyncio

from connectors.playwright_connector import (
    PlaywrightConnector
)


async def main():

    connector = PlaywrightConnector()

    content = await connector.get_page_content(
        "https://example.com"
    )

    print(
        content[:500]
    )


asyncio.run(main())