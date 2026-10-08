from app.scrapers import scraper_config
from app.source_specific_collector.all_sources_collector import (
    collect_all_sources,
)
from app.validator.validate_products import validate_products
from app.normalizer.product_normalizer import normalize_products
from app.database.dependencies import get_db
from app.database.repositories.product_repository import save_product


def collect_market_data(db):
    with scraper_config.get_session() as session:
        products, failed_sources = collect_all_sources(session)

    raw_products = validate_products(products)
    normalized_products = normalize_products(raw_products)


    try:
        for product_data in normalized_products:
            save_product(db, product_data)

        db.commit()

    except Exception:
        db.rollback()
        raise

    return normalized_products, failed_sources