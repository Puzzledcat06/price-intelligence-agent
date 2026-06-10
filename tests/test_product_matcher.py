import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.product_matcher import ProductMatcher


product_a = (
    "Apple iPhone 17 Pro 256GB Black"
)

product_b = (
    "iPhone 17 Pro 256 GB"
)

result = ProductMatcher.is_match(
    product_a,
    product_b
)

print(result)