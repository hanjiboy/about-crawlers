import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from pymongo import MongoClient

client = MongoClient()


def OPHouse(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        tbody = soup.find(id='tbdy')
        groups = tbody.find_all('optgroup')[0]
        opts = groups.find_all('option')
        items = []
        for opt in opts:
            items.append(
                opt.text.replace('\u21AA', '').replace('\u25C6', '').replace('\u2605', '').replace('\u3000', '').replace
                ('\n', '').replace('，價值', '$').replace('↘$', '↘').replace(' ', ''))
        data = []
        for item in items:
            result = re.search(r'(.+)\$(\d.+)', item)
            if '$' not in item:
                continue
            else:
                product_name = result.group(1).replace(',', '').replace('（', '')
                product_price = result.group(2).replace('）', '')
            data.append({'product_name': product_name, 'product_price': product_price})
        # pprint(data)

        for product in data:
            client.OriginalPriceHouse.itemlists.insert_one(product)
