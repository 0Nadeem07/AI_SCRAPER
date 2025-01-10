
from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
import time
# from webdriver_manager.chrome import ChromeDriverManager
import requests

def url_content(url):

    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Run in headless mode
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    
    # # Use webdriver-manager to download the appropriate ChromeDriver
    # service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service, options=options)
    response = requests.get(url)
    # driver.get(url)
    # time.sleep(2)

    # response  =  driver.page_source

    # print(response.status_code)
    if response.status_code == 200:
        soup =BeautifulSoup(response.text,'html.parser')
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