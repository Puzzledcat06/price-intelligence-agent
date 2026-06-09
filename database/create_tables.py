import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from database.base import Base
from database.connection import engine

# IMPORTANT
import database.models

Base.metadata.create_all(bind=engine)

print("Tables created successfully")