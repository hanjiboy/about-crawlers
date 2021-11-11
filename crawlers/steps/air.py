import requests
from pprint import pprint
import re


def Air(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        data = r.json()
        pprint(data)
        # name = [d for d in data if '萬華' in d['Name']][0]['Name']          拿單一監測站
        for d in data:
            try:
                name = d['Name']
                result = re.search(r'(.+)\(AQI=(\d+)', name)
                site_name = result.group(1)
                AQI = result.group(2)
                print(site_name, AQI)
            except AttributeError:
                print('not AQI !')
