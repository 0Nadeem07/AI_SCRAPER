import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def url_content(url):

    chrome_driver_path = "chromedriver.exe"
    service = Service(chrome_driver_path)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(2)

    response  =  driver.page_source

    # print(response.status_code)
    if response:
        soup =BeautifulSoup(response,'html.parser')
        body = soup.body
        if body:
            return str(body)
        else:
            return ""
        
    driver.quit()

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