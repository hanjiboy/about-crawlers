import requests
from pprint import pprint


def StockAi(url):
    r = requests.get(url + '?symbol=%5ETWII&resolution=D&from=1631606279&to=1632470279', verify=False)
    if r.status_code == requests.codes.ok:
        data = r.json()
        zippend = zip(data['t'], data['o'], data['h'], data['l'], data['c'], data['v'])     # 日期 開 高 低 收 成交量

        pprint(list(zippend))
