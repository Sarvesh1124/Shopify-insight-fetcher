Shopify Insight Fetcher

A FastAPI backend application that fetches and organizes insights from any given Shopify store (without using the official Shopify API).
The API extracts a brand’s product catalog, policies, FAQs, contact details, social media handles, and more into a well-structured JSON format.



Features

Product Catalog – Fetches the complete list of products from /products.json.

Hero Products – Products highlighted on the home page.

Policies – Privacy, Return & Refund policies.

FAQs – Extracts brand frequently asked questions.

Social Media Handles – Instagram, Facebook, TikTok, etc.

Contact Details – Emails, phone numbers.

About Brand – Brand description text.

Important Links – Order tracking, Contact Us, Blog links, etc.

RESTful API with Swagger UI (/docs).



Tech Stack

Language: Python

Framework: FastAPI

Database: (Not used in mandatory section, MySQL can be added for bonus)

Tools: Pydantic, Requests, BeautifulSoup



Project Structure
Shopify-insight-fetcher/
│── app/
│   ├── main.py          # FastAPI entry point
│   ├── models.py        # Pydantic models
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation



Setup Instructions

Clone the repository:

git clone https://github.com/Sarvesh1124/Shopify-insight-fetcher.git
cd Shopify-insight-fetcher


Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Run the server:

uvicorn app.main:app --reload


Open API documentation in browser:
http://127.0.0.1:8000/docs



Usage Example
Request

POST → /fetch-insights

{
  "website_url": "https://memy.co.in"
}

Response (sample)
{
  "brand_name": "MeMy",
  "products": [
    {"title": "Hair Growth Serum", "price": "₹799"},
    {"title": "Nourishing Shampoo", "price": "₹499"}
  ],
  "hero_products": ["Hair Growth Serum"],
  "privacy_policy": "We respect your privacy...",
  "refund_policy": "Refunds can be requested within 7 days...",
  "faqs": [
    {"question": "Do you have COD?", "answer": "Yes, we do."}
  ],
  "social_handles": {
    "instagram": "https://instagram.com/memy",
    "facebook": "https://facebook.com/memy"
  },
  "contact": {
    "email": "support@memy.co.in",
    "phone": "+91-9876543210"
  },
  "about_brand": "MeMy is a brand dedicated to hair care...",
  "important_links": {
    "order_tracking": "/pages/track-order",
    "blogs": "/blogs/news"
  }
}



Notes

Works for most Shopify stores (/products.json endpoint must be public).

Some sites may structure FAQs/policies differently; the application attempts to handle via scraping.

For bonus features, competitor analysis and MySQL persistence can be added.



You said:
yes
ChatGPT said:
