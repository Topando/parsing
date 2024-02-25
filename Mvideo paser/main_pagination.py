import json
from config import *
import requests
import os
import math


def get_data():
    params = {
        'categoryId': '65',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }
    if not os.path.exists('data'):
        os.makedirs('data')

    s = requests.Session()

    response = s.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                     headers=headers).json()
    total_items = response.get('body').get('total')

    if total_items is None:
        print('No items found')

    pages_count = math.ceil(total_items / 24)

    products_ids = {}
    products_description = {}
    products_prices = {}
    for i in range(pages_count):
        offset = f'{i * 24}'

        params = {
            'categoryId': '65',
            'offset': offset,
            'limit': '24',
            'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
            'doTranslit': 'true',
        }

        response = s.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                         headers=headers).json()
        products_ids_list = response.get('body').get('products')
        products_ids[i] = products_ids_list
        json_data = {
            'productIds':
                products_ids_list,
            'mediaTypes': [
                'images',
            ],
            'category': True,
            'status': True,
            'brand': True,
            'propertyTypes': [
                'KEY',
            ],
            'propertiesConfig': {
                'propertiesPortionSize': 5,
            },
            'multioffer': False,
        }
        response = s.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                                 json=json_data).json()
        products_description[i] = response

    # products_ids = response['body']['products']
    # file = open('1_products_ids.json', 'w', encoding='utf-8')
    # json.dump(products_ids, file, ensure_ascii=False, indent=4)
    # json_data = {
    #     'productIds':
    #         products_ids,
    #     'mediaTypes': [
    #         'images',
    #     ],
    #     'category': True,
    #     'status': True,
    #     'brand': True,
    #     'propertyTypes': [
    #         'KEY',
    #     ],
    #     'propertiesConfig': {
    #         'propertiesPortionSize': 5,
    #     },
    #     'multioffer': False,
    # }
    #
    # response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
    #                          json=json_data).json()
    # file = open('2_products.json', 'w', encoding='utf-8')
    # json.dump(response, file, ensure_ascii=False, indent=4)
    # products_ids = ','.join([i for i in products_ids])
    # params = {
    #     'productIds': products_ids,
    #     'addBonusRubles': 'true',
    #     'isPromoApplied': 'true',
    # }
    #
    # response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
    #                         headers=headers).json()
    #
    # file = open('3_prices.json', 'w', encoding='utf-8')
    # json.dump(response, file, ensure_ascii=False, indent=4)
    #
    # items_price = {}
    # material_price = response.get('body').get('materialPrices')
    # for item in material_price:
    #     item_id = item.get('productId')
    #     print(item_id)
    #     base_price = item.get('price').get('basePrice')
    #     sale_price = item.get('price').get('salePrice')
    #     bonus = item.get('bonusRubles').get('total')
    #
    #     items_price[item_id] = {
    #         'item_basePrice': base_price,
    #         'item_salePrice': sale_price,
    #         'item_bonus': bonus
    #     }
    # file = open('4_item_prices.json', 'w', encoding='utf-8')
    # json.dump(items_price, file, ensure_ascii=False, indent=4)


def get_result():
    file = open('2_products.json', 'r', encoding='utf-8')
    products_data = json.load(file)
    file = open('4_item_prices.json', 'r', encoding='utf-8')
    products_prices = json.load(file)
    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')
        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')
    file = open('5_result.json', 'w', encoding='utf-8')
    json.dump(products_data, file, ensure_ascii=False, indent=4)


get_data()
