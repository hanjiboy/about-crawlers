import requests
from pprint import pprint
from pymongo import MongoClient

client = MongoClient()


def PChome(url):
    for i in range(1, 4):
        r = requests.get(url + '?q=%E9%9B%BB%E7%AB%B6&page=1&sort=sale/dc')
        if r.status_code == requests.codes.ok:
            data = r.json()
            lists = []
            for d in data['prods']:
                product_name = d['name']
                product_price = d['price']
                lists.append({'product_name': product_name, 'product_price': product_price})
            # pprint(lists)

            for product in lists:
                client.PChome.itemlists.insert_one(product)
