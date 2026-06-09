from datetime import datetime
from uuid import uuid4

from sqlalchemy import (
    String,
    Float,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from database.base import Base


class Product(Base):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4())
    )

    brand: Mapped[str] = mapped_column(String(100))
    model: Mapped[str] = mapped_column(String(255))
    storage: Mapped[str] = mapped_column(String(50))

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    prices = relationship(
        "Price",
        back_populates="product"
    )


class Retailer(Base):
    __tablename__ = "retailers"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4())
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    prices = relationship(
        "Price",
        back_populates="retailer"
    )


class Price(Base):
    __tablename__ = "prices"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4())
    )

    product_id: Mapped[str] = mapped_column(
        ForeignKey("products.id")
    )

    retailer_id: Mapped[str] = mapped_column(
        ForeignKey("retailers.id")
    )

    price: Mapped[float] = mapped_column(Float)

    url: Mapped[str] = mapped_column(
        String(1000)
    )

    collected_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    product = relationship(
        "Product",
        back_populates="prices"
    )

    retailer = relationship(
        "Retailer",
        back_populates="prices"
    )