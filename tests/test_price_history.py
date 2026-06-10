import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.price_repository import PriceRepository

history = PriceRepository.get_price_history(
    "iphone 17 pro"
)

for item in history:

    print(
        item.price,
        item.collected_at
    )