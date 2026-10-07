from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models import Product, ProductVariant, PriceObservation
from app.models.product_data import ProductData


def save_product(
    db: Session,
    product_data: ProductData,
) -> Product:
    product = db.scalar(
        select(Product).where(
            Product.source == product_data.source,
            Product.source_product_id == product_data.source_product_id,
        )
    )

    if product is None:
        product = Product(
            source=product_data.source,
            source_product_id=product_data.source_product_id,
            product_name=product_data.product_name,
            location=product_data.location,
        )

        db.add(product)
        db.flush()

    variant = db.scalar(
        select(ProductVariant).where(
            ProductVariant.product_id == product.id,
            ProductVariant.source_variant_id
            == product_data.source_variant_id,
        )
    )

    if variant is None:
        variant = ProductVariant(
            product_id=product.id,
            source_variant_id=product_data.source_variant_id,
        )

        db.add(variant)
        db.flush()

    observation = PriceObservation(
        variant_id=variant.id,
        price=product_data.price,
        currency=product_data.currency,
        availability=product_data.availability,
        observed_at=product_data.scraped_at,
    )

    db.add(observation)

    return product