import requests
from bs4 import BeautifulSoup

def scrape_etsy_top_listing(keyword):
    # Create a search URL using Google Shopping with the provided keyword
    search_url = f"https://www.google.com/search?tbm=shop&q={keyword.replace(' ', '+')}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Send a request to Google Shopping
    response = requests.get(search_url, headers=headers)
    if response.status_code != 200:
        return "Error retrieving search results."

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all shopping result links and filter those pointing to Etsy
    links = soup.find_all('a', href=True)
    for link in links:
        href = link['href']
        if 'etsy.com' in href:
            return f"Found Etsy listing: {href}"

    return "No Etsy listing found."
