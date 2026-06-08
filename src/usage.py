from product_scraper import ProductScraper

if __name__ == "__main__":
    URL = 'https://www.mipo.com.tr'
    scraper = ProductScraper(URL)
    scraper.scrape()
