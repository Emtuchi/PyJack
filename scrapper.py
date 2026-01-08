from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import pandas as pd
import os

from utils import random_delay, clean_text, retry

# ---------------- Selenium Setup ----------------
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in background
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Optional: set user-agent for requests
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
)

service = Service("/path/to/chromedriver")  # Update path
driver = webdriver.Chrome(service=service, options=chrome_options)

# ---------------- Target URL ----------------
URL = "https://example.com/products"  # Replace with the site you want

@retry(times=3)
def get_page_html(url):
    driver.get(url)
    # Wait for page content to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".product-card"))
    )
    random_delay()
    return driver.page_source

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    products = []

    for item in soup.select(".product-card"):  # Update CSS selector
        name = item.select_one(".product-title")
        price = item.select_one(".product-price")

        products.append({
            "Name": clean_text(name.get_text()) if name else None,
            "Price": clean_text(price.get_text()) if price else None
        })
    return products

def save_data(data, folder="output"):
    os.makedirs(folder, exist_ok=True)

    # Save CSV
    df = pd.DataFrame(data)
    csv_path = os.path.join(folder, "products.csv")
    df.to_csv(csv_path, index=False)

    # Save JSON
    json_path = os.path.join(folder, "products.json")
    df.to_json(json_path, orient="records", indent=4)

    print(f"Data saved to {csv_path} and {json_path}")

# ---------------- Main Execution ----------------
if __name__ == "__main__":
    html = get_page_html(URL)
    if html:
        products = parse_html(html)
        save_data(products)
    driver.quit()
