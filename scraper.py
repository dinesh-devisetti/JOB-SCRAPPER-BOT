import requests
from bs4 import BeautifulSoup

def scrape_wellfound():
    url = "https://wellfound.com/jobs?type=software&experience=entry"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for card in soup.select("a[data-job-slug]")[:10]:
        title = card.get_text(strip=True)
        link = f"https://wellfound.com{card['href']}"
        results.append(f"{title} — {link}")
    return results
