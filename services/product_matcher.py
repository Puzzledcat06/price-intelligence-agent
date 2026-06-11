from rapidfuzz import fuzz

from services.product_normalizer import (
    ProductNormalizer
)


class ProductMatcher:

    @staticmethod
    def is_match(
        product1: str,
        product2: str,
        threshold: int = 75
    ):

        product1 = (
            ProductNormalizer.normalize(
                product1
            )
        )

        product2 = (
            ProductNormalizer.normalize(
                product2
            )
        )

        score = fuzz.token_set_ratio(
            product1,
            product2
        )

        print(
            f"Match Score: {score}"
        )

        return score >= threshold