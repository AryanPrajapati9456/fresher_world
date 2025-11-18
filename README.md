## 🌐 FreshersWorld Python Jobs Scraper

A production-grade web scraper that extracts Python job listings from FreshersWorld using Requests, BeautifulSoup, sessions, retry logic, logging, random delays, and exports data into Excel, CSV, and JSON.

This project is written with real freelancer standards — the type of scraper clients actually pay for.

# 🚀 Features

🔹 Professional Scraping

Scrapes 200+ pages safely

Uses requests.Session() for efficiency

Smart retry logic (3 attempts)

Modular design (easily extendable)

🔹 Anti-Bot Evasion

Random delays: 1.5–3.5 seconds

Realistic request headers

Predictable blocking avoided

Logs every request & failure

🔹 Multiple Export Formats

Excel (.xlsx)

CSV (.csv) — dynamic fieldnames

JSON (.json)

Files named with current date

🔹 Highly Reliable

Auto-skips broken job entries

Logs everything in fresherworld_scraper.log

Safe in long runs

Works even with partial failures

# 📁 Project Structure
freshersworld/
│── scraping.py
│── fresherworld_scraper.log
│── output/
│     ├── fresher_world_YYYY-MM-DD.xlsx
│     ├── fresher_world_YYYY-MM-DD.csv
│     └── fresher_world_YYYY-MM-DD.json
└── README.md

# 🛠 Installation

1. Clone the repository
git clone https://github.com/AryanPrajapati9456/freshersworld-scraper.git
cd freshersworld-scraper

2. Install dependencies

pip install -r requirements.txt

▶️ Running the Scraper

Simply run:

python scraper.py


Output files will appear as:

fresher_world_YYYY-MM-DD.xlsx

fresher_world_YYYY-MM-DD.csv

fresher_world_YYYY-MM-DD.json

# 🧠 How the Scraper Works

🔄 Pagination Logic

FreshersWorld uses:

offset = page_number * 20


The scraper handles this automatically for all pages.

# 🛡 Anti-Detection Techniques

Random delay between requests

Retry logic for network failures

Session-based scraping

Modern User-Agent headers

These techniques avoid temporary blocks and give the scraper a human-like footprint.

# 🧹 Data Fields Extracted

Field	Description
Role	Job title
Company Name	Employer
Location	City / location
Experience	Required experience
Salary	Salary details
Description	Job summary
Post Date	Date posted
Link	Job apply URL
📊 Example JSON Output
{
  "Role": "Python Developer",
  "Company Name": "TechCorp",
  "Location": "Bangalore",
  "Experience": "0-1 years",
  "Salary": "₹3,00,000 - ₹4,00,000",
  "Description": "Immediate opening for Python Dev...",
  "Post Date": "2 days ago",
  "Link": "/job/python-developer-12345"
}

# 🔮 Future Enhancements

Proxy rotation support

Auto-detect total pages

Command-line flags (--csv, --json, etc.)

SQLite / MongoDB export

Daily auto-scraping with cron

API wrapper version

# 📜 License

MIT License – free for commercial use.

# 👨‍💻 Author

Aryan Prajapati
Python Developer • Web Scraper • Automation Engineer

If you like this project, ⭐ star the repository on GitHub!