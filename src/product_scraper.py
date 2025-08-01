import requests
import re
import csv
import time
from bs4 import BeautifulSoup
from utilities import Utilities

class ProductScraper:
    def __init__(self, base_url):
        self.utilities = Utilities()
        self.base_url = base_url
        self.products = []

    def fetch_page(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Page not responding. Status Code: {response.status_code}")
            return None

    def find_product_links(self):
        page_content = self.fetch_page(self.base_url)
        if page_content:
            soup = BeautifulSoup(page_content, 'html.parser')
            pattern = re.compile(f"{self.base_url}/urun/")
            links = []
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                if pattern.match(href):
                    links.append(href)
            unique_links = self.utilities.listToUniqueList(links)
            return unique_links
        return []

    def extract_product_info(self, link):
        page_content = self.fetch_page(link)
        if page_content:
            soup = BeautifulSoup(page_content, 'html.parser')

            title_element = soup.find('h1', class_='product_title')
            product_name = title_element.get_text(strip=True) if title_element else "Ürün adı bulunamadı"

            price_element = soup.select_one('p.price bdi')
            price = price_element.get_text(strip=True).replace('₺', '').strip() if price_element else "Fiyat bulunamadı"

            print("Product name:", product_name)
            print("Product price:", price)
            self.products.append([product_name, price])

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['product_name', 'product_price'])
            writer.writerows(self.products)

    def scrape(self):
        start_time = time.time()
        product_links = self.find_product_links()
        for product_link in product_links:
            self.extract_product_info(product_link)
        self.save_to_csv('output/products.csv')
        end_time = time.time()
        duration = end_time - start_time
        print(f"Fetching prices from the website took {duration:.2f} seconds.")