from time import sleep
from bs4 import BeautifulSoup
from seleniumwire import webdriver
from selenium.webdriver import Proxy
from selenium.webdriver.common.proxy import ProxyType
import undetected_chromedriver as uc
import os
import json

STANDART_LINK = "https://www.ozon.ru"


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
    if not os.path.exists('data'):
        os.makedirs('data')
    driver = create_driver()
    driver.get(
        'https://www.ozon.ru/category/marshrutizatory-15855/tp-link-26303437/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=роутер+archer+c6')
    for i in range(1, 10):
        sleep(2)
        driver.execute_script(
            "var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        sleep(3.4)
        file = open(f'data/{i}_page.html', 'w', encoding='utf-8')
        file.write(driver.page_source)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        link = soup.find(class_='oe b237-a0 b237-b6 b237-b1')
        next_page = STANDART_LINK + link.get('href')
        driver.get(next_page)
        i += 1


def get_info(page):
    products_list = {}
    file = open(f'data/{page}.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(file.read(), 'lxml')
    all_el = soup.find_all(class_='i3v vi3')
    for el in all_el:
        product_list = {}
        image = el.find(class_='r9i')
        if image is not None:
            image_link = image.get('src')
            product_list['image_link'] = image_link
        link = STANDART_LINK + el.find(class_='tile-hover-target ri6 ir7').get('href')
        product_list['product_link'] = link
        name = el.find(class_='ba9 a0c c0a ri6').find('span').string
        all_settings = (el.find(class_='ba9 ri6').find('span'))
        for setting in all_settings.find_all('br'):
            if setting.next_element == 'Макс. скорость беспроводного соединения, Мбит/с: ':
                speed_wifi = setting.next_element.next_element.string
                product_list['speed_wifi'] = speed_wifi + " Мбит/с"
        product_list['SalePrice'] = el.find(class_='c3127-a1 tsHeadline500Medium c3127-c0').string
        price = el.find(class_='c3127-a1 tsBodyControl400Small c3127-b0')
        if price is not None:
            product_list["Price"] = el.find(class_='c3127-a1 tsBodyControl400Small c3127-b0').string
        products_list[name] = product_list
    file = open(f"products/{page}_products.json", "w", encoding='utf-8')
    json.dump(products_list, file, ensure_ascii=False, indent=4)


for i in range(1, 10):
    if not os.path.exists('products'):
        os.makedirs('products')
    get_info(str(i) + '_page')