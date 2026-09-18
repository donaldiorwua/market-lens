import json


def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def json_to_list(filename):

    data = load_json(filename)
    products = data["data"]["products"]["nodes"]
    product = products[0]

    print(products)
    print(product["title"])


result = json_to_list("shopify_apidata.txt")