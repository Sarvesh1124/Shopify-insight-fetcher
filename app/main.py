from fastapi import FastAPI, HTTPException
import httpx
from bs4 import BeautifulSoup

app = FastAPI(title="Shopify Insights Fetcher", version="1.0.0")


@app.get("/")
async def health_check():
    return {"message": "Shopify Insights Fetcher is running.", "version": "1.0.0"}


@app.post("/insights")
async def get_insights(data: dict):
    website_url = data.get("website_url")
    if not website_url:
        raise HTTPException(status_code=400, detail="website_url is required")

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(website_url)
            if resp.status_code != 200:
                raise HTTPException(status_code=401, detail="Website not found")

        soup = BeautifulSoup(resp.text, "lxml")

        title = soup.title.string if soup.title else "Unknown"

        return {
            "website_url": website_url,
            "brand_name": title,
            "hero_products": [],
            "whole_product_catalog": [],
            "privacy_policy": None,
            "return_refund_policy": None,
            "faqs": [],
            "social_handles": [],
            "contact_details": [],
            "important_links": []
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
