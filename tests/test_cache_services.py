import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.cache_services import CacheService


CacheService.set(
    "iphone",
    {
        "price": 1000
    }
)

result = CacheService.get(
    "iphone"
)

print(result)
