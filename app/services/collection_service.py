from app.scrapers import scraper_config
from app.source_specific_collector.all_sources_collector import collect_all_sources
from app.validator.validate_products import validate_products
from app.normalizer.product_normalizer import normalize_products

def collect_market_data():
    with scraper_config.get_session() as session:
        products, failed_sources = collect_all_sources(session)

    raw_products = validate_products(products)
    normalized_products = normalize_products(raw_products)

    return normalized_products, failed_sources