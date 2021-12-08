import logging
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from uuid import uuid4
from params import Params

PARAMS = Params()

logging.basicConfig(level=logging.INFO)

def get_content(driver, uri):
    logging.info(f"Scraping uri: {uri}")
    driver.get(uri)
    try :
        content = driver.find_element(By.ID ,"content").text
        content = content.replace("\n","")
    except Exception as e:
        print(f"Exception: {str(e)}")
        content = ""
    return content

def get_content_position( uri):
    content = ""
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    service = Service("chromedriver/chromedriver")
    driver = webdriver.Chrome(options=options, service=service)
    try :    
        driver.get(uri)
        try :
            content = driver.find_element(By.ID ,"content").text
        except Exception as e:
            print(f"Exception: {str(e)}")            
    finally :
        driver.quit()            
    return content


def get_city_maps(text):
    city = ""
    uri = PARAMS.uri_api
    text_clean = text.replace("/","")
    query = {'query':text_clean, 'key':PARAMS.key}
    response = requests.get(uri, params=query).json()
    results = response["results"]
    
    for result in results:
        if "formatted_address" in result.keys() :
            city = result["formatted_address"]
    return city
    
def scraping_uri(uri):
    logging.info(f"Scraping uri: {uri}")
    positions = []
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    service = Service("chromedriver/chromedriver")
    driver = webdriver.Chrome(options=options, service=service)
    try :
            
        driver.get(uri)
        results = driver.find_elements(By.CLASS_NAME ,"opening")

        for result in results :        
            position = {}
            link = result.find_element(By.XPATH,"a")
            position["id"] = uuid4()
            position["name"] = link.text
            position["uri"] = link.get_attribute('href')
            position["location"] = result.find_element(By.CLASS_NAME,"location").text
            position["country"] = ""
            position["description"] = ""        
            positions.append(position)
        
        for position in positions :
            position["description"] = get_content(driver,position["uri"])
            
    finally :
        driver.quit()
        
    return positions

def obtain_data(position):
    position["country"] = get_city_maps(position["location"])
    return position

