import json
from app.normalizer import product_normalizer

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def json_to_list(filename):
    data = load_json(filename)

    products = data["data"]["products"]["nodes"]

    result = []

    for product in products:
        title = product["title"]
        variants = product["variants"]["nodes"]

        for variant in variants:
            variant_dict = {
                "product_name": title,
                "price": variant["price"]["amount"],
                "currency": variant["price"]["currencyCode"],
                "availability": variant["availableForSale"],
                "location": "Nigeria",
                "source": "Brandlyng"
            }
            result.append(variant_dict)

    return result

raw_dicts = json_to_list("shopify_apidata.txt")
raw_products = product_normalizer.validate_products(raw_dicts)
products = product_normalizer.validate_products(raw_products)
print(raw_products)