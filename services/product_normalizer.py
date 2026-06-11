import re


class ProductNormalizer:

    COLORS = [
        "black",
        "white",
        "blue",
        "green",
        "purple",
        "titanium",
        "gold",
        "silver"
    ]

    @staticmethod
    def normalize(title: str):

        normalized = title.lower()

        for color in ProductNormalizer.COLORS:
            normalized = normalized.replace(
                color,
                ""
            )

        normalized = re.sub(
            r"\d+\s?gb",
            "",
            normalized,
            flags=re.IGNORECASE
        )

        normalized = " ".join(
            normalized.split()
        )

        return normalized.strip()