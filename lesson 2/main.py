import json

import requests
from bs4 import BeautifulSoup
import lxml
import csv
# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}
#
# req = requests.get(url, headers=headers)
# src = req.text
# file = open("index.html", "w", encoding="utf-8")
# file.write(src)
# file = open("index.html", encoding="utf-8")
# src = file.read()
# soup = BeautifulSoup(src, "lxml")
# all_a = soup.find_all(class_="mzr-tc-group-item-href")
# all_a_dict = {}
# for a in all_a:
#     all_a_dict[a.text] = "https://health-diet.ru" + a.get("href")
#
# file = open("all_a_dict.json", "w", encoding="utf-8")
# json.dump(all_a_dict, file, ensure_ascii=False, indent=4)


file = open("all_a_dict.json", encoding="utf-8")
all_categories = json.load(file)
count = 0
for name, href in all_categories.items():
    rep = [",", " ", "-"]
    for item in rep:
        if item in name:
            name = name.replace(item, "_")
    req = requests.get(href, headers=headers)
    src = req.text
    file = open(f"templates/{count}_{name}.html", "w", encoding="utf-8")
    file.write(src)
    file = open(f"templates/{count}_{name}.html", "r", encoding="utf-8")
    src = file.read()
    soup = BeautifulSoup(src, "lxml")
    if soup.find(class_="uk-alert-danger") is None:
        th_tegs = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
        product = th_tegs[0].text
        calories = th_tegs[1].text
        proteins = th_tegs[2].text
        fats = th_tegs[3].text
        carbohydrates = th_tegs[4].text
        file = open(f"templates/{count}_{name}.csv", "w", encoding="utf-8")
        writer = csv.writer(file)
        writer.writerow(
            (
                product,
                calories,
                proteins,
                fats,
                carbohydrates,
            )
        )
        tr_in_tbody = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")
        for item in tr_in_tbody:
            product_tds = item.find_all("td")
            title = product_tds[0].text
            calories = product_tds[1].text
            proteins = product_tds[2].text
            fats = product_tds[3].text
            carbohydrates = product_tds[4].text
            file = open(f"templates/{count}_{name}.csv", "a", encoding="utf-8")
            writer = csv.writer(file)
            writer.writerow(
                (
                    title,
                    calories,
                    proteins,
                    fats,
                    carbohydrates,
                )
            )

    count += 1
