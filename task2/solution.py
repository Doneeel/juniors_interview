import requests
from bs4 import BeautifulSoup
from collections import defaultdict


def find_next_page(soup: BeautifulSoup) -> str:
    base_url = "https://ru.wikipedia.org"

    link = soup.find("a", string="Следующая страница")

    if link is None:
        return None

    link = link.get("href")

    return base_url + link


def parse_page(soup: BeautifulSoup) -> list:
    animals = list()

    links = soup.find(
        "div", attrs={"class": "mw-category mw-category-columns"}
    ).find_all("ul")

    for link in links:
        animals.extend(link.text.split("\n"))

    return animals


def run():
    page_counter = 0
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"

    letters_dict = defaultdict(int)

    while url is not None:
        if page_counter > 300:
            break

        print(f"[TASK2] Processing page number {page_counter}")
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        url = find_next_page(soup)
        if url is None:
            break

        animals = parse_page(soup)

        for animal in animals:
            letters_dict[animal[0]] += 1

        page_counter += 1

    with open("animals.csv", "w", encoding="UTF-8") as csv_file:
        csv_file.writelines(
            [f"{letter[0]},{letter[1]}\n" for letter in letters_dict.items()]
        )
