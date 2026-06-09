from connectors.flipkart_connector import FlipkartConnector
from connectors.amazon_connector import AmazonConnector


class ConnectorManager:

    def __init__(self):

        self.connectors = [
            FlipkartConnector(),
            AmazonConnector()
        ]

    async def search_product(self, query: str):

        all_products = []

        for connector in self.connectors:

            products = await connector.search_product(query)

            all_products.extend(products)

        return all_products