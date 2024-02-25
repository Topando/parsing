from time import sleep

import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from seleniumwire import webdriver


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


driver = create_driver()
driver.get("https://www.avito.ru/")
try:
    input_fild = driver.find_element(By.CLASS_NAME, "input-input-Zpzc1")
    input_fild.send_keys("DASDA")
    sleep(1)
    input_fild.send_keys(Keys.ENTER)
except Exception:
    driver.quit()
sleep(5)
driver.quit()
