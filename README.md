# MIPO Scraper

A robust and efficient Python-based web scraper designed to extract product information from the [MIPO](https://www.mipo.com.tr) e-commerce platform. This tool automates the collection of product names and prices, making it easy to analyze market data and track price changes.

---

## Key Features

- **Efficient Web Scraping**: Leverages BeautifulSoup and requests library for fast and reliable page fetching
- **Product Data Extraction**: Automatically extracts product names and prices from product pages
- **Duplicate Removal**: Ensures unique product links are processed, eliminating redundant data collection
- **CSV Export**: Exports collected product data directly to CSV format for easy analysis and integration
- **Error Handling**: Robust error handling for network issues and missing data
- **Performance Tracking**: Monitors and reports scraping duration for performance analysis
- **User-Friendly**: Simple API with straightforward configuration

---

## Getting Started

These instructions will help you set up and run the MIPO Scraper on your local machine for development and scraping purposes.

### Prerequisites

Before running this project, ensure you have the following installed:

- **Python**: Version 3.7 or higher
  - Check your version: `python --version`
- **pip**: Python package manager (usually included with Python)
  - Check your version: `pip --version`
- **Git**: For cloning the repository (optional)

### Installation

Follow these steps to install and set up the project:

1. **Clone the repository** (or download the ZIP file):
   ```bash
   git clone https://github.com/basaran3mir/mipo-scraper.git
   cd mipo-scraper
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Basic Usage

Run the scraper with default settings:

```bash
python examples/usage_example.py
```

### Code Example

Here's how to use the scraper in your own Python script:

```python
from src.product_scraper import ProductScraper

# Initialize the scraper with the target URL
scraper = ProductScraper('https://www.mipo.com.tr')

# Perform the scraping operation
scraper.scrape()

# The results are automatically saved to output/products.csv
```

### Output

The scraper generates a CSV file (`output/products.csv`) with the following structure:

```
product_name,product_price
Product Name 1,199.99
Product Name 2,299.99
...
```

---

## Project Structure

```
mipo-scraper/
│
├── src/                          # Main source code directory
│   ├── product_scraper.py       # Core scraper class
│   └── utils.py                 # Utility functions
│
├── examples/                      # Example scripts
│   └── usage_example.py          # Basic usage example
│
├── output/                        # Output directory (generated)
│   └── products.csv              # Scraped product data
│
├── venv/                          # Virtual environment (local only)
│
├── requirements.txt               # Project dependencies
├── README.md                      # This file
├── LICENSE                        # License information
└── .gitignore                     # Git ignore rules
```

---

## Configuration

### Current Settings

The scraper currently uses default configuration pointing to:
- **Base URL**: `https://www.mipo.com.tr`
- **Output File**: `output/products.csv`

### Customization

To modify the scraper behavior, edit the `examples/usage_example.py` file:

```python
URL = 'https://www.mipo.com.tr'  # Change this URL if needed
scraper = ProductScraper(URL)
scraper.scrape()
```

### Output Location

To change the output filename, modify the `scrape()` method in `src/product_scraper.py`:

```python
self.save_to_csv('your_custom_filename.csv')
```

---

## Development

### Project Dependencies

The project uses the following libraries (see `requirements.txt`):

- **requests**: HTTP library for fetching web pages
- **beautifulsoup4**: HTML parsing and web scraping
- Other standard Python libraries: csv, re, time

### Setting Up Development Environment

1. Create and activate a virtual environment (see Installation section)
2. Install dependencies with `pip install -r requirements.txt`
3. Make your changes to the source code
4. Test your changes with `python examples/usage_example.py`

### Code Structure

- **ProductScraper Class**: Main class handling the scraping logic
  - `fetch_page()`: Retrieves page content via HTTP
  - `find_product_links()`: Extracts product URLs from category pages
  - `extract_product_info()`: Parses individual product pages
  - `save_to_csv()`: Exports data to CSV format
  - `scrape()`: Orchestrates the complete scraping workflow

- **Utils Class**: Helper utility functions
  - `list_to_unique_list()`: Removes duplicate entries from lists

---

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository on GitHub
2. **Create a feature branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** and test thoroughly
4. **Commit with clear messages**:
   ```bash
   git commit -m "Add description of your changes"
   ```
5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request** with a description of your changes

### Guidelines

- Follow PEP 8 style guidelines for Python code
- Add comments for complex logic
- Test your changes before submitting a PR
- Keep commits atomic and well-documented

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For questions, feature requests, or bug reports, please open an issue in this repository.
