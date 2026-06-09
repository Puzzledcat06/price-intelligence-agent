class PriceAnalyzer:

    @staticmethod
    def get_lowest_price(products):

        return min(
            products,
            key=lambda p: p.price
        )