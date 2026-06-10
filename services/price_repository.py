from database.connection import SessionLocal
from database.models import Product, Retailer, Price


class PriceRepository:

    @staticmethod
    def save_price_snapshot(product_data):

        db = SessionLocal()

        try:

            retailer = (
                db.query(Retailer)
                .filter(
                    Retailer.name == product_data.retailer
                )
                .first()
            )

            if not retailer:
                raise Exception(
                    f"Retailer not found: {product_data.retailer}"
                )

            product = (
                db.query(Product)
                .filter(
                    Product.model == product_data.title
                )
                .first()
            )

            if not product:

                product = Product(
                    brand="Unknown",
                    model=product_data.title,
                    storage="Unknown"
                )

                db.add(product)
                db.commit()
                db.refresh(product)

            price_record = Price(
                product_id=product.id,
                retailer_id=retailer.id,
                price=product_data.price,
                url=product_data.url
            )

            db.add(price_record)
            db.commit()

            print(
                f"Saved price for {product_data.title}"
            )

        except Exception as e:

            db.rollback()

            print(
                f"Error saving price: {e}"
            )

        finally:

            db.close()

    @staticmethod
    def get_price_history(product_name: str):

        db = SessionLocal()

        try:

            product = (
                db.query(Product)
                .filter(
                    Product.model == product_name
                )
                .first()
            )

            if not product:
                return []

            history = (
                db.query(Price)
                .filter(
                    Price.product_id == product.id
                )
                .all()
            )

            return history

        finally:

            db.close()

    @staticmethod
    def get_latest_price(product_name: str):

        db = SessionLocal()

        try:

            product = (
                db.query(Product)
                .filter(
                    Product.model == product_name
                )
                .first()
            )

            if not product:
                return None

            latest_price = (
                db.query(Price)
                .filter(
                    Price.product_id == product.id
                )
                .order_by(
                    Price.collected_at.desc()
                )
                .first()
            )

            return latest_price

        finally:

            db.close()

    @staticmethod
    def get_cheapest_price(product_name: str):

        db = SessionLocal()

        try:

            product = (
                db.query(Product)
                .filter(
                    Product.model == product_name
                )
                .first()
            )

            if not product:
                return None

            cheapest_price = (
                db.query(Price)
                .filter(
                    Price.product_id == product.id
                )
                .order_by(
                    Price.price.asc()
                )
                .first()
            )

            return cheapest_price

        finally:

            db.close()