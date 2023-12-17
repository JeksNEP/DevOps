from bs4 import BeautifulSoup
import requests
from database.db import create_db, Database


headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.731 YaBrowser/23.11.1.731 Yowser/2.5 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
}


def generate_url() -> str:
    for url_page in range(1,3):
        main_url = f"https://www.vsemayki.ru/catalog/view/manwear?sort=new&page={url_page}&scroll=true"

        response = requests.get(main_url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all("div", class_="_1GrkkIVc")

        for i in data:
            item_url = r"https://www.vsemayki.ru/" + i.find("div", class_="_2o6OVoxH").find("a").get("href")
            yield item_url


def get_info():
    for product_url in generate_url():
        with Database().get_connection() as con:
            cur = con.cursor()
            new_response = requests.get(product_url, headers=headers)
            new_soup = BeautifulSoup(new_response.text, "lxml")

            product_name = new_soup.find("div", class_="_16SQsX8u").find("span", class_="product__info-name").text
            product_type = new_soup.find("div", class_="_16SQsX8u").find("span", class_="product__info-model").text
            product_price = new_soup.find("div", class_="ai0y7-SB").find("span", class_="price--1I8Le").text
            product_description = new_soup.find("div", class_="_1IB1ndiZ").find("p", class_="_2rtXh5hp").text
            product_url_image = new_soup.find("img").get("src")

            cur.execute('''
                INSERT INTO products (product_name, product_type, product_price, product_url_image, product_description, product_url)
                VALUES (?, ?, ?, ?, ?, ?) 
                ''', (product_name, product_type, product_price, product_url_image, product_description, product_url))
            con.commit()
get_info()