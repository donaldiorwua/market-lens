from app.scrapers import scraper_config
import requests

def collect_brandlyng_products(session):
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

    try:
        response = session.post(
            url,
            json=payload,
            headers=headers,
            timeout=10
        )
        
        response.raise_for_status()
    except requests.exceptions.RequestException as error:
        return [], error
        
    data = response.json()
    if data.get("errors"):
        messages = [err.get("message", "Unknown GraphQL error") for err in data["errors"]]
        error = Exception("GraphQL error(s): " + "; ".join(messages))
        return [], error
    
    products = data["data"]["products"]["nodes"]
    if not products:
        error = Exception("No products found from Brandlyng")
        return [], error
    
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

    return result, None