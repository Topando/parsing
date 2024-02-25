import json

from bs4 import BeautifulSoup
import requests
from config import *
import math
import os


def get_product_imgs(id):
    vol = id // 100_000
    if (vol >= 0 and vol <= 143):
        host = "01"
    elif (vol >= 144 and vol <= 287):
        host = "02"
    elif (vol >= 288 and vol <= 431):
        host = "03"
    elif (vol >= 432 and vol <= 719):
        host = "04"
    elif (vol >= 720 and vol <= 1007):
        host = "05"
    elif (vol >= 1008 and vol <= 1061):
        host = "06"
    elif (vol >= 1062 and vol <= 1115):
        host = "07"
    elif (vol >= 1116 and vol <= 1169):
        host = "08"
    elif (vol >= 1170 and vol <= 1313):
        host = "09"
    elif (vol >= 1314 and vol <= 1601):
        host = "10"
    elif (vol >= 1602 and vol <= 1655):
        host = "11"
    elif (vol >= 1656 and vol <= 1919):
        host = "12"
    elif (vol >= 1920 and vol <= 2045):
        host = "13"
    else:
        host = "14"
    url = f'https://basket-{host}.wbbasket.ru/vol{vol}/part{id // 1000}/{id}/images/c516x688/1.webp'
    return url


def get_data():
    s = requests.Session()
    # min_price = 1500 * 100
    # max_price = 15000 * 100
    for i in range(1, get_pages() + 1):
        try:
            params = {
                'appType': '1',
                'curr': 'rub',
                'dest': '-1257786',
                'page': f'{i}',
                'preset': '158137',
                'sort': 'popular',
                'spp': '30',
                'xsubject': '105',
                # 'priceU': f'{min_price};{max_price}',
                # 'fsize': '36422'
            }
            response = s.get('https://search.wb.ru/promo/bucket_3/catalog', params=params, headers=headers).json()
        except Exception:
            exit(0)
        products_list = response.get('data').get('products')
        product_items = {}
        for product in products_list:
            product_id = product['id']
            product_rating = product['reviewRating']
            product_name = product['name']
            product_price = product['salePriceU']
            product_brand = product['brand']
            product_feedbacks = product['feedbacks']
            product_imgs_url = get_product_imgs(product_id)
            product_url = f'https://www.wildberries.ru/catalog/{product_id}/detail.aspx'
            product_items[product_id] = {
                'product_name': product_name,
                'product_brand': product_brand,
                'product_price': product_price / 100,
                'product_rating': product_rating,
                'product_feedbacks': product_feedbacks,
                'product_imgs_url': product_imgs_url,
                'product_url': product_url,
            }
        if not os.path.exists('data'):
            os.makedirs('data')
        file = open(f"data/{i}_products.json", "w", encoding='utf-8')
        json.dump(product_items, file, ensure_ascii=False, indent=4)
        print(i)


def get_pages():
    params = {
        'appType': '1',
        'curr': 'rub',
        'dest': '-1257786',
        'preset': '158137',
        'spp': '30',
    }

    response = requests.get('https://search.wb.ru/promo/bucket_3/v4/filters', params=params, headers=headers).json()
    count_products = int(response.get('data').get('total'))
    count_pages = math.ceil(count_products / 100)
    return count_pages


get_data()
