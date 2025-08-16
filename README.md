# Shopify Insights Fetcher

A FastAPI backend application that fetches insights from Shopify-powered stores without using the official Shopify API.

---

## Features
- Fetches whole product catalog via `/products.json`
- Extracts hero products (from home page)
- Collects Privacy Policy and Return/Refund Policy
- Extracts FAQs if present
- Finds Social Media Handles (Instagram, FB, TikTok, etc.)
- Collects Contact details (emails, phone numbers)
- Extracts Brand context text (About Us section)
- Finds Important links (Order Tracking, Blogs, Contact Us)

---

## Installation & Run
```bash
# clone repo
git clone https://github.com/USERNAME/shopify-insights-fetcher.git
cd shopify-insights-fetcher

# create virtual environment
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run server
uvicorn app.main:app --reload
```

Server runs at:  
 http://127.0.0.1:8000  

---

##  API Endpoints

### Health Check
`GET /`
```json
{
  "message": "Shopify Insights Fetcher is running.",
  "version": "1.0.0"
}
```

### Fetch Insights
`POST /insights`  
Request:
```json
{
  "website_url": "https://memy.co.in"
}
```
Response:
```json
{
  "website_url": "https://memy.co.in",
  "brand_name": "MeMy",
  "hero_products": [],
  "whole_product_catalog": [],
  "privacy_policy": "...",
  "return_refund_policy": "...",
  "faqs": [],
  "social_handles": ["https://instagram.com/..."],
  "contact_details": ["support@memy.co.in"],
  "important_links": ["https://memy.co.in/pages/contact"]
}
```

---

## Tests
```bash
pytest
```
