from app.models import product_data
from typing import List


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
        availability = raw_data.availability,
        scraped_at = raw_data.scraped_at
    )

def normalize_products(raw_products: List[product_data.RawProductData]) -> List[product_data.ProductData]:
    products_data = []
    for raw_product in raw_products:
        normalized_product = normalize_product(raw_product)
        products_data.append(normalized_product)
    return products_data

raw_products = [
    product_data.RawProductData(
        product_name="  Samsung Galaxy A15  ",
        price="28000",
        currency=" ngn ",
        location=" Lagos ",
        source="Example Store",
        availability=True
    ),
    product_data.RawProductData(
        product_name="  iPhone 15 ",
        price="450000",
        currency=" usd ",
        location=" Abuja ",
        source="Another Store",
        availability=True
    )
]


def validate_product(raw_dict: dict) -> product_data.RawProductData:
    raw_product = product_data.RawProductData.model_validate(raw_dict) 

    return raw_product


def validate_products(raw_dicts: List[dict]) -> List[product_data.RawProductData]:
    raw_products = [
        validate_product(item)
        for item in raw_dicts
    ]

    return raw_products


products = validate_products(raw_products)
for product in products:
    print(product)