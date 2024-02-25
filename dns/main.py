from time import sleep

from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from selenium.webdriver import Proxy
from selenium.webdriver.common.proxy import ProxyType
import undetected_chromedriver as uc
import os
import json


def create_driver():
    my_options = webdriver.ChromeOptions()
    my_options.add_argument('--log-level=3')
    my_options.add_argument('--no-sandbox')
    my_options.add_argument('--disable-dev-shm-usage')
    my_options.add_argument('--disable-blink-features=AutomationControlled')
    my_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
    my_options.add_argument('--no-first-run')  # this might be specific to undetected_chromedriver.v2 only
    my_options.add_argument('--no-service-autorun')  # this might be specific to undetected_chromedriver.v2 only
    my_options.add_argument('--password-store=basic')  # this might be specific to undetected_chromedriver.v2 only
    # my_options.add_experimental_option( 'useAutomationExtension', False )
    # my_options.add_experimental_option( 'excludeSwitches', ( 'enable-automation', ) )
    my_options.add_argument('--start-maximized')
    my_options.add_argument('--blink-settings=imagesEnabled=false')
    try:
        return uc.Chrome(options=my_options)
    except Exception:
        print("0(")


def get_data():
    for i in range(100):
        sleep(1)
        driver.execute_script(
            "var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        sleep(2)
        try:
            button = driver.find_element(By.CLASS_NAME, "pagination-widget__show-more-btn")
            driver.execute_script("arguments[0].click();", button)
        except Exception:
            file = open("pages.html", 'w', encoding='utf-8')
            file.write(driver.page_source)
            break

driver = create_driver()
driver.get(
    "https://www.dns-shop.ru/catalog/17a8aa1c16404e77/wi-fi-routery/?order=6&stock=now-today-tomorrow-later-out_of_stock")
get_data()
