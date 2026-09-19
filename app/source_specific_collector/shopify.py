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


    response = requests.post(session)
    
    data = response.json()
