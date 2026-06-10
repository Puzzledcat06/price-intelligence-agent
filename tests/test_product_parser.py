import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.product_parser import ProductParser


sample = (
    "Apple iPhone 17 Pro 256GB Black Titanium"
)

result = ProductParser.parse(
    sample
)

print(result)