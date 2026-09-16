from app.models import product_data
import datetime


def normalize_product(raw_data: product_data.RawProductData) -> product_data.ProductData:
    normalized_product_name = raw_data.product_name.strip()
    normalized_location = raw_data.location.strip()
    normalized_currency = raw_data.currency.strip().upper()

    return product_data.ProductData(
        product_name = normalized_product_name,
        price = raw_data.price,
        currency = normalized_currency,
        location = normalized_location,
        source = raw_data.source,
        availability = raw_data.availability
    )



product = [{
    "product_id": "550e8400-e29b-41d4-a716-446655440000",
    "product_name": "Samsung Galaxy A15",
    "price": "28000",         
    "currency": "NGN",
    "location": "Lagos",
    "source": "Example Store",
    "availability": True,
    "scraped_at": datetime 
}]


validated = normalize_product(product)

print(validated)