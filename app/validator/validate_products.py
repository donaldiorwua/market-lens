from app.models import product_data
from typing import List

def validate_product(raw_dict: dict) -> product_data.RawProductData:
    raw_product = product_data.RawProductData.model_validate(raw_dict) 

    return raw_product


def validate_products(raw_dicts: List[dict]) -> List[product_data.RawProductData]:
    raw_products = [
        validate_product(item)
        for item in raw_dicts
    ]

    return raw_products
