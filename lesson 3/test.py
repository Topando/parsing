import json

from bs4 import BeautifulSoup
import requests

file = open("all.json", "r", encoding="utf-8")
data = json.load(file)
res = {}
data_dict = []
count = 0
for name, href in data.items():
    url = href
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    company = soup.find(class_="bt-biografie-name").find("h3").text.strip().split(", ")[-1]
    links = soup.find(class_="bt-linkliste").find_all("a")
    array_links = []
    for link in links:
        array_links.append(link.get("href"))

    data = {
        'name': name,
        'company': company,
        'links': array_links,
    }
    data_dict.append(data)
    count += 1
    if count == 12:
        break
file = open("data.json", "w", encoding="utf-8")
json.dump(data_dict, file, indent=4)
