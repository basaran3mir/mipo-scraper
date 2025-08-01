# Mipo Product Info Scraper 🛠️📦

This is a Python project developed for a corporate use case. In real use case it's working on server-side. It scrapes product names and prices from the [Mipo](https://www.mipo.com.tr) website and updates the internal AI-powered customer support bot's database automatically.

## 📌 Purpose

At my current company, I manage a mobile phone brand that has an official website. I previously developed an AI supported chatbot for this website, which answers customer queries by referring to a structured response database.

However, since product information such as pricing or model availability may change over time, it's crucial that the chatbot database stays up to date. This project solves that problem by scraping the website periodically and updating the chatbot's database with the latest product info.

## 🚀 Features

- ✅ Fetches product names and current prices from the product pages
- ✅ Automatically extracts data from dynamic HTML content using BeautifulSoup
- ✅ Prevents duplicate product entries
- ✅ Updates the chatbot's backend data (integration handled server-side)
- ✅ CSV export support
- ✅ JSON database update functionality

## ⚙️ Technologies Used

- `Python 3`
- `requests`
- `BeautifulSoup`
- `re (regex)`
- `csv`, `json` for file operations

## 🧠 How It Works

1. Scraper visits the main site and gathers all product page links.
2. For each product:
   - Extracts the product name from `<h1 class="product_title">`.
   - Extracts the price from `<p class="price"><bdi>...</bdi></p>`.
3. Updates a local JSON file that acts as the AI bot’s response database.