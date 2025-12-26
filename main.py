from scraper import scrape_wellfound
from emailer import send_email

def main():
    jobs = []
    jobs.extend(scrape_wellfound())
    if not jobs:
        print("No jobs found today.")
        return

    content = "\n\n".join(jobs)
    send_email(content)
    print(f"Sent {len(jobs)} job listings via email.")

if __name__ == "__main__":
    main()

