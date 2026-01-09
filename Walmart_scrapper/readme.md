# Walmart Product Scraper (Python)

## 📌 Overview

This project is a Python-based web scraper that collects structured product information from Walmart’s website.

The script searches for multiple product categories, navigates through search result pages, visits individual product pages, extracts useful product data, and stores everything in a structured output file.

In simple terms, it acts like an automated shopper that browses Walmart and writes down product details.

---

## 🎯 Features

- Searches Walmart using predefined keywords
- Crawls through multiple search result pages
- Extracts individual product page links
- Visits each product page
- Parses embedded JSON data from the page
- Collects product details such as price, ratings, and availability
- Avoids duplicate product URLs
- Uses proxies to reduce blocking
- Implements retries and exponential backoff for reliability
- Saves results in JSON Lines format (`.jsonl`)

---

## 📦 Data Extracted Per Product

Each product record includes:

- Product name
- Brand
- Price
- Availability status
- Average rating
- Total review count
- Item ID
- Product image URL
- Short description

Each product is written as **one JSON object per line** in the output file.

---

## 🛠 Tech Stack

- Python 3
- requests
- BeautifulSoup (bs4)
- json
- queue
- python-dotenv
- HTTP proxies

---

## 🧠 How the Script Works

1. Loads proxy credentials from environment variables
2. Sends requests with browser-like headers
3. Searches Walmart for predefined product keywords
4. Extracts product links from search result pages
5. Stores product URLs in a queue to avoid duplicates
6. Opens each product page
7. Extracts structured product data from embedded JSON
8. Writes product data to an output file
9. Retries failed requests with exponential backoff

---
