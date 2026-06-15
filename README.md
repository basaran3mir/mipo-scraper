# MIPO Scraper

A lightweight Python web scraper for extracting product names and prices from the MIPO website and saving them to a CSV file.

## Key features

- Extracts product links from the MIPO homepage
- Scrapes product names and prices from individual product pages
- Removes duplicate product URLs before scraping
- Saves results to `output/products.csv`
- Simple and easy to run with a small codebase

## Getting Started

These instructions will help you get a local copy of the project up and running for development and testing purposes.

### Prerequisites

- Python 3.10 or newer
- `pip` package manager
- Internet access to fetch product pages from `https://www.mipo.com.tr`

### Install

1. Clone the repository:

```bash
git clone https://github.com/basaran3mir/mipo-scraper.git
cd mipo-scraper
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
.\\venv\\Scripts\\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the scraper from the `src` directory or from the project root:

```bash
python src/usage.py
```

The scraper will fetch product page links from the base URL, extract product details, and write them to `output/products.csv`.

## Project Structure

- `README.md` - Project overview and setup instructions
- `requirements.txt` - Python dependencies
- `src/`
  - `product_scraper.py` - Main scraper implementation
  - `usage.py` - Entry point for running the scraper
  - `utils.py` - Utility helper functions
- `output/` - Generated output files
  - `products.csv` - Scraped product data
- `LICENSE` - Project license

## Configuration

The base target URL is defined in `src/usage.py`:

```python
URL = 'https://www.mipo.com.tr'
```

If you need to target a different base URL or change the output path, update this value or modify the `ProductScraper` implementation accordingly.

## Development

For local development, use the existing virtual environment and dependency file.

- Add new scraping logic in `src/product_scraper.py`
- Keep utility helpers in `src/utils.py`
- Use `print()` statements for lightweight debugging

To rerun the scraper after changes:

```bash
python src/usage.py
```

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to your branch (`git push origin feature-name`)
5. Open a pull request

Please ensure code is clean and maintainable, and document any new behavior clearly.

## License

This project is covered under the license in the `LICENSE` file.

## Contact

For questions, feature requests, or bug reports, please open an issue in this repository.
