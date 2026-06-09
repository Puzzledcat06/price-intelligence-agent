from connectors.base_connector import BaseConnector

from services.product_schema import ProductData


class FlipkartConnector(BaseConnector):

    async def search_product(self, query: str):

        return [
            ProductData(
                title=query,
                price=1000,
                url="https://example.com",
                retailer="Flipkart"
            )
        ]