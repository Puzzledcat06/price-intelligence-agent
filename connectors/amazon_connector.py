from connectors.base_connector import BaseConnector
from services.product_schema import ProductData


class AmazonConnector(BaseConnector):

    async def search_product(self, query: str):

        return [
            ProductData(
                title=query,
                price=1200,
                url="https://amazon.in/example",
                retailer="Amazon"
            )
        ]