import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.price_repository import PriceRepository

cheapest = PriceRepository.get_cheapest_price(
    "iphone 17 pro"
)

print(cheapest.price)