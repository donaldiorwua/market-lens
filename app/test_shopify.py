import requests
import json

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

url = "https://brandlyng.myshopify.com/api/2026-07/graphql.json"

query = """
{
    products(first: 5) {
        nodes {
            id
            title
            handle
            variants(first: 5) {
                nodes {
                    price {
                        amount
                        currencyCode
                    }
                    availableForSale
                }
            }
        }
    }
}
"""

payload = {
    "query": query
}

headers = {
    "Content-Type": "application/json"
}


response = requests.post(
    url,
    json=payload,
    headers=headers,
    timeout=10
)

print("Status code:", response.status_code)
data = response.json()
save_json(data, "shopify_apidata.txt")