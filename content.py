
from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
import time
# from webdriver_manager.chrome import ChromeDriverManager
import requests
import logging
import pandas as pd
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()  # loads variables from .env into environment


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

endpoint = os.getenv("ONIONFLEET_API_ENDPOINT")
result_endpoint_base = os.getenv("ONIONFLEET_RESULT_ENDPOINT")
def start_scraping(url):
    payload = {"url": url, "is_html": False}
    try:
        response = requests.post(endpoint, json=payload, timeout=10)
        data = response.json()
        return data.get("token")
    except Exception as e:
        logger.error(f"Error starting scrape for {url}: {e}")
        return None

def get_scraped_html(token, max_retries=10, delay=8):

    result_endpoint = f"{result_endpoint_base}{token}"
    for _ in range(max_retries):
        try:
            response = requests.get(result_endpoint, timeout=10)
            content_type = response.headers.get("Content-Type", "")

            if "application/json" in content_type:
                data = response.json()
                status = data.get("status")
                if status == "SUCCESS":
                    return response.text
                elif status == "FAILED":
                    logger.warning(f"Scrape failed for token: {token}")
                    return None
                else:
                    logger.info(f"Status: {status}. Retrying...")
                    time.sleep(delay)
            else:
                return response.text
        except Exception as e:
            logger.warning(f"Error fetching result for token {token}: {e}")
            time.sleep(delay)
    return None


def url_content(url):

#     options = webdriver.ChromeOptions()
#     # options.add_argument("--headless")  # Run in headless mode
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
    
#     # Use webdriver-manager to download the appropriate ChromeDriver
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)

#     # proxy = {
#     #     'https://':"3.99.167.1:3128",
#     # }

#     # headers = {
#     #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
#     # }
#     # response = requests.get(url ,headers=headers)
#     # print(response.status_code)
#     driver.get(url)
#     time.sleep(2)

#     response  =  driver.page_source
    token = start_scraping(url)
    logger.info(f"Your token , {token}")

    if not token:
        logger.error(f"Failed to start scrape for {url}")

    html = get_scraped_html(token)
    if not html:
        logger.error(f"Failed to get HTML for {url}")
    soup =BeautifulSoup(html,'html.parser')
    body = soup.body
    if body:
        return str(body)
    else:
        return ""
        
        
    # driver.quit()

def clean_content(body):
    if body:
        soup = BeautifulSoup(body ,'html.parser')
        for script_or_style in soup(['style', 'script']):
            script_or_style.extract()

        cleaned_content = soup.get_text(separator='\n')
        cleaned_content = "\n".join(
            line.strip() for line in cleaned_content.splitlines() if line.strip()
        )
    

    return cleaned_content

def split_dom_content(dom_content ,max_length =6000):

    return [
        dom_content[i:i+max_length] for i in range(0 , len(dom_content),max_length)
        ]


# res =url_content('https://www.techwithtim.net/')
# print(res)