

def collect_all_sources(session):
    products = []
    failed_sources = []
    
    collectors = [
        (collect_brandlyng_products, "Brandlyng"),
        (collect_mock_products, "Mock"),
    ]
    for collector, source in collectors:
        collector_products, error = collector(session)

        if error is None:
            products.extend(collector_products)
        else:
            failed_sources.append({
                "source": source,
                "error": error
            })

    return products, failed_sources