import requests
from pymongo import MongoClient

client = MongoClient()


def SinYa(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        data = r.json()
        lists = []
        for d in data:
            product_name = d['prod_name']
            product_price = d['price']
            if product_price == '0':
                continue
            else:
                lists.append({'product_name': product_name, 'product_price': product_price})

        for product in lists:
            client.SinYa.itemlists.insert_one(product)
