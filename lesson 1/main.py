import re

from bs4 import BeautifulSoup

file = open("templates/index 1.html", encoding="utf-8")
src = file.read()

soup = BeautifulSoup(src, "lxml")

# title = soup.title.text

# page_h1 = soup.find("h1") находит первый элемент
# page_h1_all = soup.find_all("h1")) находит все элементы


# username = soup.find("div", class_="user__name").find("span")


# username = soup.find("div", {"class": "user__name", "id": "username"}).find("span").text  можно передавать словарь


# user_info = soup.find("div", class_="user__info")


# links = soup.find(class_="social__networks").find_all("a")
# for link in links:
#     print(link.get("href")) выдает атрибут


# .find_parent() .find_parents() ищет родителей (((
# post_div = soup.find("div", class_="post__text").find_parent("div", class_="user__post") ищет первого родителя
# post_div = soup.find("div", class_="post__text").find_parents() ищет всех родителей до тега html

# .next_element() .previous_element() следующий и предыдущий
# next_el = soup.find(class_='user__name').next_element.next_element
# previous_el = soup.find(class_='123').previous_element.previous_element

# find_next_sibling() .find_previous_sibling() следующий и предыдущий элемент внутри тега
# next_sibling = soup.find(class_="user__birth__date").find_previous_sibling()


# print(soup.find("h3", string="Wi-Fi Hack"))
# print(soup.find(string=re.compile("Wi-Fi")))
# print(soup.find_all(string=re.compile("[Ww]i-Fi")))