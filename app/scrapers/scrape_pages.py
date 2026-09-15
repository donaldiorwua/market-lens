from app.scrapers import scraper_config
from app.scrapers import scrape_page
import requests
def pages_scraper(base_url, pages):
    all_articles = []
    failed_pages = []

    with scraper_config.get_session() as session:
  
        for page in range (1, pages + 1):
            try:
                page_url = f"{base_url}?p={page}"
                articles = scrape_page.page_scraper(page_url, session)
                for article in articles:
                    article["page"] = page
                all_articles.extend(articles)
            except requests.RequestException as e:
                failed_pages.append({"page": page, "error": str(e)})

    return all_articles, failed_pages