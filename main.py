import re
from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL = "https://www.ts.kg/category/films"
HEADERS = {
    "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


def get_data_from_page():
    response = requests.get(url=URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_="app-shows-item-full")
    films = []
    for item in items:
        film = {
            "title": item.find("span", class_="app-shows-card-title").text.strip(),
            "link": "https://www.ts.kg" + item.find("a").get("href"),
            "caption": item.find("span", class_="app-shows-card-tooltip").text.strip()
        }
        films.append(film)




    #pprint(films)



get_data_from_page()
