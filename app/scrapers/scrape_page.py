from app.scrapers import fetcher
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import datetime

def page_scraper(url, session):
    articles = []

    html = fetcher.fetcher(url, session)
    soup = BeautifulSoup(html, "html.parser")

    title_lines = soup.find_all("span", class_="titleline")
    
    if title_lines:
        for title_line in title_lines:
            a_tag = title_line.find("a")
            if a_tag:
                href = a_tag.get("href")
                title_link = a_tag.get_text(strip=True)
                if href:
                    link = urljoin(url, href)
                    title = title_link
                else:
                    link = None
                    title = title_link    
            else:
                link = None
                title = title_line.get_text(strip=True)
            article = {
                "title": title,
                "link": link,
                "scraped_at": datetime.datetime.now().isoformat()
            }

            articles.append(article)
    else:
        raise Exception(f"No articles found at the URL: {url}")

    return articles
