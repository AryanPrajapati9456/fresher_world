# 🐍 FreshersWorld Python Jobs Analytics & Scraper

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

A production-grade web scraper and analytics tool that extracts Python job listings from **FreshersWorld**. 
Built with **Requests**, **BeautifulSoup**, and **Streamlit**, it mimics human behavior to safely scrape over 200+ pages of job content.

---

## 🎥 Project Demo



https://github.com/user-attachments/assets/740ec8a3-096a-497a-82df-85ce5ab694a7



---

## 🚀 Features

### 🖥️ Interactive Dashboard
- **Controls**: Set strict page limits (1-200) via the sidebar.
- **Live Feedback**: Real-time progress bar and streaming logs.
- **Instant Export**: Download data in **Excel**, **CSV**, or **JSON** immediately.
- **Data Metrics**: Quick view of total jobs and unique companies found.

### 🛡️ Smart Scraping Core
- **Anti-Bot Evasion**: Uses `requests.Session()` with realistic headers and random delays (1.5-3.5s).
- **Retry Logic**: Automatically retries failed requests up to 3 times.
- **Resilience**: Skips broken entries without crashing the entire process.
- **Logging**: Detailed logging to both the UI and `fresherworld_scraper.log`.

---

## 📥 Extracted Data

| Field | Description |
| :--- | :--- |
| **Role** | Job Title (e.g., Python Developer) |
| **Company** | Hiring Organization |
| **Location** | City / Remote status |
| **Experience** | Years required |
| **Salary** | Compensation range |
| **Link** | Direct application URL |

---

## 🛠️ Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/AryanPrajapati9456/freshersworld-scraper.git
    cd freshersworld-scraper
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Dashboard**
    ```bash
    streamlit run app.py
    ```
    *Open the URL shown in your terminal (usually `http://localhost:8501`).*

---

## 📁 Project Structure

```text
├── app.py                  # 🎨 Streamlit App (Entry Point)
├── scraping.py             # 🧠 Core Scraping Logic
├── fresherworld_scraper.log # 📝 Runtime logs
├── requirements.txt        # 📦 Dependencies
├── README.md               # 📄 Documentation
```

---

## ⚠️ Ethical Note
This tool is for **educational and portfolio purposes**. Please respect FreshersWorld's `robots.txt` and Terms of Service. Do not scrape aggressively.

---

## 👨‍💻 Author
**Aryan Prajapati**
*Python Developer • Web Scraper • Automation Engineer*

[![GitHub](https://img.shields.io/badge/GitHub-AryanPrajapati9456-181717?style=flat&logo=github)](https://github.com/AryanPrajapati9456)
