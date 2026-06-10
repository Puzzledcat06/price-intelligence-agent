from rapidfuzz import fuzz


class ProductMatcher:

    @staticmethod
    def is_match(
        product1: str,
        product2: str,
        threshold: int = 75
    ):

        score = fuzz.token_set_ratio(
            product1.lower(),
            product2.lower()
        )

        print(f"Match Score: {score}")

        return score >= threshold