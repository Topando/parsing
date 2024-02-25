import time

import requests
from selenium import webdriver


def get_data(url):
    headers = {'User-Agent': 'Mozilla/5'}
    req = requests.get(url, headers=headers)
    file = open('data.html', 'w', encoding='utf-8')
    file.write(req.text)
    file.close()


def get_data_w(url):
    options = webdriver.FirefoxOptions()
    options.set_preference('general.useragent.override', 'Mozilla/5.0 (')
    driver = webdriver.Firefox()
    try:
        driver.get(url)
    except Exception as e:
        print(e)

    file = open('data.html', 'w', encoding='utf-8')
    file.write(driver.page_source)
    driver.close()
    driver.quit()


def main():
    get_data_w(
        'https://www.youtube.com/')


if __name__ == '__main__':
    main()
