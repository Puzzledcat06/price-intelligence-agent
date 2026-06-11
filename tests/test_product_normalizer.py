import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.product_normalizer import (
    ProductNormalizer
)

result = ProductNormalizer.normalize(
    "Apple iPhone 17 Pro 256GB Black Titanium"
)

print(result)