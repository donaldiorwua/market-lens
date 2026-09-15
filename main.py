from app.scrapers import scrape_pages

def main():

    articles = scrape_pages.pages_scraper("https://news.ycombinator.com/", 2)
    print(articles)


if __name__ == "__main__":
    main()