from app.scrapers import fetcher, scraper_config

def main():

    #articles = scrape_pages.pages_scraper("https://news.ycombinator.com/", 2)
    #print(articles)
    session = scraper_config.get_session()

    html = fetcher.fetcher("https://www.jumia.com.ng/vivo-y11d-6.74-120hz-1286gb-6500mah-44w-fast-charge-gold-420136959.html", session)

    scraper_config.save_json(html, "jumia_html")

if __name__ == "__main__":
    main()