import streamlit as st
import pandas as pd
import json
import time
import io
import logging
from scraping import scrape_jobs

# Configure Streamlit page
st.set_page_config(
    page_title="FresherWorld Scraper",
    page_icon="🐍",
    layout="wide"
)

# Custom logging handler to display logs in Streamlit
class StreamlitHandler(logging.Handler):
    def __init__(self, container):
        super().__init__()
        self.container = container
        self.text = ""

    def emit(self, record):
        try:
            msg = self.format(record)
            self.text += msg + "\n"
            self.container.code(self.text, language="text")
        except Exception:
            pass

st.title("🐍 FresherWorld Python Jobs Scraper")
st.markdown("Extract Python job listings professionally. Use this interface to control the scraper safely.")

# Sidebar for controls
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Allow user to choose number of pages
    max_pages = st.number_input(
        "Pages to Scrape", 
        min_value=1, 
        max_value=214, 
        value=5, 
        help="Total pages available: ~214. Each page takes ~2-4 seconds."
    )
    
    start_btn = st.button("Start Scraping", type="primary")
    
    st.info(f"⏱ Estimated time: ~{max_pages * 3} seconds")

# Main area
if start_btn:
    st.header("📊 Live Execution Feedback")
    
    # Progress indicators
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Log container
    log_expander = st.expander("Show Live Logs", expanded=True)
    with log_expander:
        log_container = st.empty()
    
    # Setup custom logging
    logger = logging.getLogger()
    # Remove existing handlers to avoid duplication if re-run
    # but be careful not to remove the file handler if needed. 
    # Just add ours.
    handler = StreamlitHandler(log_container)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)
    
    try:
        # Progress callback
        def on_progress(page, total):
            progress = page / total
            progress_bar.progress(progress)
            status_text.text(f"⏳ Scraping page {page} of {total}...")
        
        # Run scraper
        with st.spinner("Initializing scraper..."):
            data = scrape_jobs(max_pages=max_pages, progress_callback=on_progress)
        
        # Completion
        progress_bar.progress(100)
        status_text.success(f"✅ Scraping Completed! Found {len(data)} jobs.")
        
        # Display Data
        st.header("📋 Scraped Data")
        if data:
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
            
            # Metrics
            col1, col2 = st.columns(2)
            col1.metric("Total Jobs", len(df))
            col2.metric("Unique Companies", df['Company Name'].nunique() if 'Company Name' in df else 0)

            # Download Section
            st.header("📥 Download Results")
            d1, d2, d3 = st.columns(3)
            
            # CSV
            csv = df.to_csv(index=False).encode('utf-8')
            d1.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"fresher_world_{time.strftime('%Y%m%d')}.csv",
                mime="text/csv",
            )
            
            # JSON
            json_data = json.dumps(data, indent=4, ensure_ascii=False).encode('utf-8')
            d2.download_button(
                label="Download JSON",
                data=json_data,
                file_name=f"fresher_world_{time.strftime('%Y%m%d')}.json",
                mime="application/json",
            )
            
            # Excel
            try:
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False)
                
                d3.download_button(
                    label="Download Excel",
                    data=buffer.getvalue(),
                    file_name=f"fresher_world_{time.strftime('%Y%m%d')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )
            except Exception as ex:
                d3.error("Excel export failed.")
        else:
            st.warning("No jobs found. Check logs for details.")

    except Exception as e:
        status_text.error(f"An error occurred: {e}")
        st.error(str(e))
    finally:
        # Clean up handler
        logger.removeHandler(handler)

else:
    # Initial State
    st.info("Select the number of pages in the sidebar and click **Start Scraping**.")
    st.markdown("### How it works")
    st.markdown("""
    1. **Connects** to FreshersWorld.
    2. **Iterates** through pages with random delays to mimic human behavior.
    3. **Extracts** Python job roles, salaries, and company details.
    4. **Presents** clean data for export.
    """)
