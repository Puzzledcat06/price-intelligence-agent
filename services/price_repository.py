from database.connection import SessionLocal
from database.models import Product, Retailer, Price


class PriceRepository:

    @staticmethod
    def save_price_snapshot(product_data):

        db = SessionLocal()

        try:

            # Find retailer
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

            # Find product
            product = (
                db.query(Product)
                .filter(
                    Product.model == product_data.title
                )
                .first()
            )

            # Create product if missing
            if not product:

                product = Product(
                    brand="Unknown",
                    model=product_data.title,
                    storage="Unknown"
                )

                db.add(product)
                db.commit()
                db.refresh(product)

            # Create price snapshot
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