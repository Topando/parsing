import json

from bs4 import BeautifulSoup
import requests

all_ = {}
for i in range(0, 758, 12):
    url = f"https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=12&noFilterSet=true&offset={i}"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    elements = soup.find_all(class_="bt-slide")
    for element in elements:
        a = element.find(class_="bt-slide-content").find("a")
        name = a.get("title")
        link = a.get("href")
        all_[name] = link
file = open("all.json", "w", encoding="utf-8")
json.dump(all_, file, ensure_ascii=False, indent=4)