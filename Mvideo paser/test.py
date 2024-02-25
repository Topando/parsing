import json

import requests


def get_data():
    cookies = {
        '_ym_uid': '1688765836935970262',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_GUEST_ID': '23488818362',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_REGION_ID': '1',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_YANDEX_WIDGET': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'HINTS_FIO_COOKIE_NAME': '1',
        'searchType2': '3',
        'COMPARISON_INDICATOR': 'false',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'deviceType': 'desktop',
        'MVID_GEOLOCATION_NEEDED': 'false',
        'utm_term': 'mvideo',
        '_ym_d': '1706363151',
        'tmr_lvid': '135e5b6784519bff2737267af0b7e397',
        'tmr_lvidTS': '1688765838993',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '68a26d6c-a0ba-490d-b83e-50363a47e9ad',
        'flocktory-uuid': '4f291fc6-aeb4-4df6-ad72-2470562cf1e7-3',
        'adrcid': 'AHv8Ls7ZRHcZCV_twauNtrg',
        'afUserId': 'a8d50744-4e4f-4688-9cd6-38666df9ce7b-p',
        'adid': '170636315150281',
        '_gpVisits': '{"isFirstVisitDomain":true,"idContainer":"100025D5"}',
        'MVID_FILTER_CODES': 'true',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICE_AVLB': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        '_ga': 'GA1.1.1730993920.1706363151',
        '__lhash_': 'd8885db6ba6c400a660ee28b90ef5209',
        'MVID_AB_PERSONAL_RECOMMENDS': 'true',
        'MVID_AB_UPSALE': 'true',
        'MVID_ACCESSORIES_PDP_BY_RANK': 'true',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_CASCADE_CMN': 'true',
        'MVID_CHAT_VERSION': '6.6.0',
        'MVID_CREDIT_DIGITAL': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_DISPLAY_ACCRUED_BR': 'true',
        'MVID_EMPLOYEE_DISCOUNT': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_NEW_CHAT_PDP': 'true',
        'MVID_NEW_GET_SHOPPING_CART_HIT_PRODUCTS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_POST_SHOPPING_CART_AUTHORIZE': 'true',
        'MVID_NEW_POST_SHOPPING_CART_USEFUL_PRODUCTS': 'true',
        'MVID_PODELI_PDP': 'true',
        'MVID_PROMO_PAGES_ON_2': 'true',
        'MVID_SERVICES': '111',
        'MVID_SINGLE_CHECKOUT': 'true',
        'MVID_SP': 'true',
        'MVID_ENVCLOUD': 'prod2',
        'mindboxDeviceUUID': 'c540d757-0510-435b-a86c-2d5dd2dba107',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22c540d757-0510-435b-a86c-2d5dd2dba107%22%7D',
        '__SourceTracker': 'https%3A%2F%2Fya.ru%2F__referral',
        'admitad_deduplication_cookie': 'other_referral',
        'SMSError': '',
        'authError': '',
        '_ym_isad': '1',
        'advcake_track_id': 'f4073f4d-cfba-bdca-abea-14526dd7cf4c',
        'advcake_session_id': 'c9601a3e-77b1-adac-a08c-76ad25bb8d40',
        'AF_SYNC': '1708327726519',
        '_sp_id.d61c': 'b267903b-7c5c-480c-b401-aedd1ba7fbc2.1688765836.3.1708327840.1706363165.6d4a5705-c926-4ee7-86f8-2ea1becf9cd0.cc38861a-b133-477c-bcf7-fef67f2f5bf1.c889c878-fda9-4fde-a293-0dea6000705b.1708327667334.32',
        'tmr_detect': '0%7C1708327844729',
        '_gp100025D5': '{"hits":2,"vc":1,"ac":1,"a6":1}',
        'gsscgib-w-mvideo': 'l8HS+lZJ60MlWQWsLJSzB9FcPonaDy+ZASHuXSW19XO/1x22ZMlwu7OYK66eAW+3OOSI6wHdSu/hgATm+80HowODarrRuPxsm/+XeDgestqa6fJI3MGi1Cy53h0oO+TG1Sfx6wn3JwG8t5BuLFh+Y+rWgf/SEzx21KOgkiI127GZMNPdKrb6CMrqUnmReiROwaRUqgEt+o/4nLKNaZNJ9YtVRUp8SOuUYAFsK/Oqu1qo3ZUAYNNtffFhmDY4SfE=',
        'gsscgib-w-mvideo': 'l8HS+lZJ60MlWQWsLJSzB9FcPonaDy+ZASHuXSW19XO/1x22ZMlwu7OYK66eAW+3OOSI6wHdSu/hgATm+80HowODarrRuPxsm/+XeDgestqa6fJI3MGi1Cy53h0oO+TG1Sfx6wn3JwG8t5BuLFh+Y+rWgf/SEzx21KOgkiI127GZMNPdKrb6CMrqUnmReiROwaRUqgEt+o/4nLKNaZNJ9YtVRUp8SOuUYAFsK/Oqu1qo3ZUAYNNtffFhmDY4SfE=',
        'fgsscgib-w-mvideo': 'AdrH886fa172400908278208c29278fede2a47e6',
        'fgsscgib-w-mvideo': 'AdrH886fa172400908278208c29278fede2a47e6',
        'gsscgib-w-mvideo': '9+olwg6ZvXbWKaXAkCTTMoWKSd3WxmEL0nDl97UbT1yNWu3aX5Cb3PnbovXU8JfEFMeqOja3yHwB4p/tt22qKEOvvrPY5zEBm+w7agN/1RxNLOxEGWvh4tCTqcMZyyyE2oQZpYW+OH6JBrcC+8uj1hJ/2+UV+hdYajJ8hnuiWV7zM6dIRSoNBYJf55zI1Y043fw1yFJF06Li241aseefSpT6dPzgjzAds7nKmvrm+iFpLmJPQtYpBTRAJpgJu84=',
        'cfidsgib-w-mvideo': '/Uo66Bzn5LFSkGIL25VTD2uiDze42uPCqn9hhOLsNF6EDZFwvXfGH7BY/nXZ+iX3w7yiVcaMb6d9qYhukiyxDHQW5RvJYUJl6xl31beUF71Yi9/DvhPsLWANkta4KMV2+A32fpUO0nvLlNwukc7oP5JVrKnoXt0VRA68Fg==',
        '__hash_': 'fa92d321dfd8b386e76455e40c711437',
        '_ga_CFMZTSS5FM': 'GS1.1.1708329905.3.0.1708329905.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1708329905.3.0.1708329905.60.0.0',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9',
        'baggage': 'sentry-environment=production,sentry-release=release_24_2_3(5919),sentry-public_key=ae7d267743424249bfeeaa2e347f4260,sentry-trace_id=909e468a057b4d36a5bf420e83239fe9,sentry-sample_rate=0.5,sentry-transaction=%2F**%2F,sentry-sampled=false',
        # 'cookie': '_ym_uid=1688765836935970262; MVID_CITY_ID=CityCZ_975; MVID_GUEST_ID=23488818362; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_REGION_ID=1; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=true; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; HINTS_FIO_COOKIE_NAME=1; searchType2=3; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; deviceType=desktop; MVID_GEOLOCATION_NEEDED=false; utm_term=mvideo; _ym_d=1706363151; tmr_lvid=135e5b6784519bff2737267af0b7e397; tmr_lvidTS=1688765838993; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=68a26d6c-a0ba-490d-b83e-50363a47e9ad; flocktory-uuid=4f291fc6-aeb4-4df6-ad72-2470562cf1e7-3; adrcid=AHv8Ls7ZRHcZCV_twauNtrg; afUserId=a8d50744-4e4f-4688-9cd6-38666df9ce7b-p; adid=170636315150281; _gpVisits={"isFirstVisitDomain":true,"idContainer":"100025D5"}; MVID_FILTER_CODES=true; MVID_FLOCKTORY_ON=true; MVID_KLADR_ID=7700000000000; MVID_NEW_LK_OTP_TIMER=true; MVID_REGION_SHOP=S002; MVID_SERVICE_AVLB=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; _ga=GA1.1.1730993920.1706363151; __lhash_=d8885db6ba6c400a660ee28b90ef5209; MVID_AB_PERSONAL_RECOMMENDS=true; MVID_AB_UPSALE=true; MVID_ACCESSORIES_PDP_BY_RANK=true; MVID_ALFA_PODELI_NEW=true; MVID_CASCADE_CMN=true; MVID_CHAT_VERSION=6.6.0; MVID_CREDIT_DIGITAL=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_DISPLAY_ACCRUED_BR=true; MVID_EMPLOYEE_DISCOUNT=true; MVID_FILTER_TOOLTIP=1; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_NEW_CHAT_PDP=true; MVID_NEW_GET_SHOPPING_CART_HIT_PRODUCTS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_POST_SHOPPING_CART_AUTHORIZE=true; MVID_NEW_POST_SHOPPING_CART_USEFUL_PRODUCTS=true; MVID_PODELI_PDP=true; MVID_PROMO_PAGES_ON_2=true; MVID_SERVICES=111; MVID_SINGLE_CHECKOUT=true; MVID_SP=true; MVID_ENVCLOUD=prod2; mindboxDeviceUUID=c540d757-0510-435b-a86c-2d5dd2dba107; directCrm-session=%7B%22deviceGuid%22%3A%22c540d757-0510-435b-a86c-2d5dd2dba107%22%7D; __SourceTracker=https%3A%2F%2Fya.ru%2F__referral; admitad_deduplication_cookie=other_referral; SMSError=; authError=; _ym_isad=1; advcake_track_id=f4073f4d-cfba-bdca-abea-14526dd7cf4c; advcake_session_id=c9601a3e-77b1-adac-a08c-76ad25bb8d40; AF_SYNC=1708327726519; _sp_id.d61c=b267903b-7c5c-480c-b401-aedd1ba7fbc2.1688765836.3.1708327840.1706363165.6d4a5705-c926-4ee7-86f8-2ea1becf9cd0.cc38861a-b133-477c-bcf7-fef67f2f5bf1.c889c878-fda9-4fde-a293-0dea6000705b.1708327667334.32; tmr_detect=0%7C1708327844729; _gp100025D5={"hits":2,"vc":1,"ac":1,"a6":1}; gsscgib-w-mvideo=l8HS+lZJ60MlWQWsLJSzB9FcPonaDy+ZASHuXSW19XO/1x22ZMlwu7OYK66eAW+3OOSI6wHdSu/hgATm+80HowODarrRuPxsm/+XeDgestqa6fJI3MGi1Cy53h0oO+TG1Sfx6wn3JwG8t5BuLFh+Y+rWgf/SEzx21KOgkiI127GZMNPdKrb6CMrqUnmReiROwaRUqgEt+o/4nLKNaZNJ9YtVRUp8SOuUYAFsK/Oqu1qo3ZUAYNNtffFhmDY4SfE=; gsscgib-w-mvideo=l8HS+lZJ60MlWQWsLJSzB9FcPonaDy+ZASHuXSW19XO/1x22ZMlwu7OYK66eAW+3OOSI6wHdSu/hgATm+80HowODarrRuPxsm/+XeDgestqa6fJI3MGi1Cy53h0oO+TG1Sfx6wn3JwG8t5BuLFh+Y+rWgf/SEzx21KOgkiI127GZMNPdKrb6CMrqUnmReiROwaRUqgEt+o/4nLKNaZNJ9YtVRUp8SOuUYAFsK/Oqu1qo3ZUAYNNtffFhmDY4SfE=; fgsscgib-w-mvideo=AdrH886fa172400908278208c29278fede2a47e6; fgsscgib-w-mvideo=AdrH886fa172400908278208c29278fede2a47e6; gsscgib-w-mvideo=9+olwg6ZvXbWKaXAkCTTMoWKSd3WxmEL0nDl97UbT1yNWu3aX5Cb3PnbovXU8JfEFMeqOja3yHwB4p/tt22qKEOvvrPY5zEBm+w7agN/1RxNLOxEGWvh4tCTqcMZyyyE2oQZpYW+OH6JBrcC+8uj1hJ/2+UV+hdYajJ8hnuiWV7zM6dIRSoNBYJf55zI1Y043fw1yFJF06Li241aseefSpT6dPzgjzAds7nKmvrm+iFpLmJPQtYpBTRAJpgJu84=; cfidsgib-w-mvideo=/Uo66Bzn5LFSkGIL25VTD2uiDze42uPCqn9hhOLsNF6EDZFwvXfGH7BY/nXZ+iX3w7yiVcaMb6d9qYhukiyxDHQW5RvJYUJl6xl31beUF71Yi9/DvhPsLWANkta4KMV2+A32fpUO0nvLlNwukc7oP5JVrKnoXt0VRA68Fg==; __hash_=fa92d321dfd8b386e76455e40c711437; _ga_CFMZTSS5FM=GS1.1.1708329905.3.0.1708329905.0.0.0; _ga_BNX5WPP3YK=GS1.1.1708329905.3.0.1708329905.60.0.0',
        'referer': 'https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65?from=under_search',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '909e468a057b4d36a5bf420e83239fe9-9da60b6a70a7290a-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36',
        'x-set-application-id': '99dc490d-2237-4b58-85a6-0d7b8d183923',
    }

    params = {
        'categoryId': '65',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    products_ids = response['body']['products']
    file = open('1_products_ids.json', 'w', encoding='utf-8')
    json.dump(products_ids, file, ensure_ascii=False, indent=4)
    json_data = {
        'productIds':
            products_ids,
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

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()
    file = open('2_products.json', 'w', encoding='utf-8')
    json.dump(response, file, ensure_ascii=False, indent=4)
    products_ids = ','.join([i for i in products_ids])
    params = {
        'productIds': products_ids,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    file = open('3_prices.json', 'w', encoding='utf-8')
    json.dump(response, file, ensure_ascii=False, indent=4)

    items_price = {}
    material_price = response.get('body').get('materialPrices')
    for item in material_price:
        item_id = item.get('productId')
        print(item_id)
        base_price = item.get('price').get('basePrice')
        sale_price = item.get('price').get('salePrice')
        bonus = item.get('bonusRubles').get('total')

        items_price[item_id] = {
            'item_basePrice': base_price,
            'item_salePrice': sale_price,
            'item_bonus': bonus
        }
    file = open('4_item_prices.json', 'w', encoding='utf-8')
    json.dump(items_price, file, ensure_ascii=False, indent=4)


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


get_result()