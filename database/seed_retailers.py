import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.connection import SessionLocal
from database.models import Retailer

db = SessionLocal()

retailers = [
    "Amazon",
    "Flipkart",
    "Myntra",
    "Ajio",
    "Meesho"
]

for retailer_name in retailers:

    existing = (
        db.query(Retailer)
        .filter(Retailer.name == retailer_name)
        .first()
    )

    if not existing:
        retailer = Retailer(name=retailer_name)
        db.add(retailer)

db.commit()

print("Retailers seeded successfully")

db.close()