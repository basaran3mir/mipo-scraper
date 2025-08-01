from product_scraper import ProductScraper

if __name__ == "__main__":
    scraper = ProductScraper('https://www.mipo.com.tr')
    scraper.scrape()
