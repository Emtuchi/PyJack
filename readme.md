# Web Scraper Project

This project is a Python-based web scraper that extracts structured data from dynamic websites using **Selenium** and **BeautifulSoup**. Extracted data is cleaned and saved in **CSV** and **JSON** formats. The scraper includes request headers, random delays, and error handling for reliability.

---

## Project Structure

---

## Features

- Handles **JavaScript-rendered dynamic content** with Selenium.
- Implements **random delays and user-agent headers** to mimic human browsing.
- Includes **retry logic** for robust scraping.
- Cleans and structures extracted data into **CSV** and **JSON** formats.
- Easily extendable for **pagination** or **infinite scroll**.

---

## Installation & Setup

### 1. Clone the Project

```bash
git clone <your-repo-url>
cd web_scraper_project

```

### 2. (Optional) Create a Virtual Environment

- It is recommended to keep dependencies isolated.

```bash
# macOS/Linux
python -m venv venv
source venv/bin/activate

# Windows (Command Prompt)
python -m venv venv
venv\Scripts\activate

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. ChromeDriver Setup

## Selenium requires a browser driver. You have two options:

- Option 1: Manual download

---

Download ChromeDriver from https://chromedriver.chromium.org/downloads

Make sure it matches your Chrome version.

## Update the path in scraper.py:

service = Service("/path/to/chromedriver")

- Option 2: Automatic management with webdriver-manager

---

Already installed in our dependencies.

## The scraper automatically downloads and uses the correct ChromeDriver version.

### Running the Scraper

```
Open scraper.py and update the target URL:

URL = "https://example.com/products"


Adjust the CSS selectors in scraper.py to match the website:
```

# Example selectors

---

.product-card
.product-title
.product-price

Run the scraper:

```bash
python scraper.py
```

The extracted data will be saved in the output/ folder as:

products.csv

## products.json
