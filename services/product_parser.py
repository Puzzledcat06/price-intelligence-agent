import re


class ProductParser:

    @staticmethod
    def parse(title: str):

        storage_match = re.search(
            r"(\d+)\s?GB",
            title,
            re.IGNORECASE
        )

        storage = (
            storage_match.group(1) + "GB"
            if storage_match
            else "Unknown"
        )

        brand = "Unknown"

        brands = [
            "Apple",
            "Samsung",
            "OnePlus",
            "Xiaomi",
            "Realme"
        ]

        for b in brands:
            if b.lower() in title.lower():
                brand = b
                break

        return {
            "brand": brand,
            "model": title,
            "storage": storage
        }