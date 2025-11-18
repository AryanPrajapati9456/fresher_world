import time
import random
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import pandas as pd
import logging
import csv
import json

logging.basicConfig(
    filename='fresher_world/fresherworld_scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

BASE_URL = "https://www.freshersworld.com/python-jobs/3535127"
LIMIT = 20
TOTAL_PAGES = 214


def safe_text(parent, tag, class_name):
    try:
        element = parent.find(tag, class_=class_name)
        return element.get_text(strip=True) if element else None
    except AttributeError as e:
        logging.error(f"safe_text error: {e}")
        return None

def safe_attr(parent, tag, class_name, attr):
    try:
        element = parent.find(tag, class_=class_name)
        return element.get(attr) if element else None
    except AttributeError as e:
        logging.error(f"safe_attr error: {e}")
        return None


def fetch_page(session, url):
    for attempt in range(3):  
        try:
            response = session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logging.error(f"[Attempt {attempt+1}] Error fetching {url} → {e}")
            time.sleep(2)
    logging.error(f"❌ Failed after 3 attempts: {url}")
    return None

def parse_jobs(html):
    jobs_list = []
    if html:
        soup = BeautifulSoup(html, "lxml")
        jobs = soup.find_all("div", class_="col-md-12 col-lg-12 col-xs-12 padding-none job-container jobs-on-hover top_space")
        dates = soup.find_all("div", class_="text-ago")

        for date, job in zip(dates, jobs):
            try:
                Role_name = safe_text(job, "span", "wrap-title seo_title")
                company_name = safe_text(job, "h3", "latest-jobs-title font-16 margin-none inline-block company-name")
                Location = safe_text(job, "a", "bold_font")
                Experience = safe_text(job, "span", "experience job-details-span")
                Salary = safe_text(job, "span", "qualifications display-block modal-open pull-left job-details-span")
                Description = safe_text(job, "span", "desc")
                Post_date = safe_text(date, "span", "ago-text")
                job_link = job.get("job_display_url")  

                jobs_list.append({
                    "Role": Role_name,
                    "Company Name": company_name,
                    "Location": Location,
                    "Experience": Experience,
                    "Salary": Salary,
                    "Description": Description,
                    "Post Date": Post_date,
                    "Link": job_link
                })
            except Exception as e:
                logging.warning(f"⚠️ Skipping a job due to unexpected error: {e}")

    return jobs_list


def scrape_jobs():
    logging.info("🟢 Scraper started")
    print("Scraper started 🟢")

    all_jobs = []
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116 Safari/537.36"
    })

    for page in range(TOTAL_PAGES):
        if page == 0:
            url = BASE_URL
        else:
            url = f"{BASE_URL}?&limit={LIMIT}&offset={LIMIT * page}"

        logging.info(f"Scraping page {page + 1}: {url}")
        print(f"➡ Scraping page {page + 1}...")

        html = fetch_page(session, url)
        page_jobs = parse_jobs(html)
        all_jobs.extend(page_jobs)

        time.sleep(random.uniform(1.5, 3.5))

    logging.info("🟢 Scraper finished")
    print("Scraper finished 🟢")
    return all_jobs


def save_csv(data):
    try:
        file_name = f"fresher_world/fresher_world_{datetime.now().strftime('%Y-%m-%d')}.csv"
        with open(file_name, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        logging.info(f"CSV saved: {file_name}")
        print(f"✅ CSV saved: {file_name}")
    except Exception as e:
        logging.error(f"Error saving CSV: {e}")

def save_json(data):
    try:
        file_name = f"fresher_world/fresher_world_{datetime.now().strftime('%Y-%m-%d')}.json"
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        logging.info(f"JSON saved: {file_name}")
        print(f"✅ JSON saved: {file_name}")
    except Exception as e:
        logging.error(f"Error saving JSON: {e}")

def save_excel(data):
    if data:
        filename = f"fresher_world/fresher_world_{datetime.now().strftime('%Y-%m-%d')}.xlsx"
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        logging.info(f"Excel saved: {filename}")
        print(f"✅ Excel saved: {filename}")
    else:
        logging.warning("No data to save.")
        print("⚠️ No data to save.")

if __name__ == "__main__":
    data = scrape_jobs()
    save_excel(data)
    save_csv(data)
    save_json(data)
