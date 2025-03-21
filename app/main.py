from fastapi import FastAPI
from app import prompts, scraper

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Etsy AI Product Generator"}

@app.get("/generate")
def generate_product(keyword: str, style: str):
    original = scraper.scrape_etsy_top_listing(keyword)
    transformed = prompts.reimagine_listing(original, style)
    return {"original": original, "transformed": transformed}
