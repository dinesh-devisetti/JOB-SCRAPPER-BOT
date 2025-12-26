import requests

def scrape_wellfound():
    url = "https://wellfound.com/jobs?type=software&experience=entry"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://wellfound.com/",
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)

        if response.status_code == 403:
            print("[WARN] Wellfound blocked the request (403). Skipping source.")
            return []

        if response.status_code != 200:
            print(f"[WARN] Wellfound returned {response.status_code}. Skipping source.")
            return []

        html = response.text

        # TODO: parse HTML and extract jobs
        return []

    except requests.RequestException as e:
        print(f"[ERROR] Wellfound request failed: {e}")
        return []
