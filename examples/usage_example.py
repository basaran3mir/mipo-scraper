import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(root_dir, "src"))

from product_scraper import ProductScraper

if __name__ == "__main__":
    URL = 'https://www.mipo.com.tr'
    scraper = ProductScraper(URL)
    scraper.scrape()
