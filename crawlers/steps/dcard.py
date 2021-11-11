import requests
from bs4 import BeautifulSoup


def DCard(url):
    ROOT_URL = url
    data = {}
    for i in range(50):
        search_url = ROOT_URL + '/b/' + str(i + 1)
        r = requests.get(search_url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            name = soup.find('div', class_='sc-1o474rp-0 iJIBfM').text
            comment = soup.find('div', class_='phqjxq-0 gFINpq').text
            if name in data:
                data[name].append(comment)
            else:
                data[name] = [comment]

    comment_list = []
    for key in data:
        comment_list.append((key, len(data[key])))
    print(sorted(comment_list, key=lambda x: x[1]))
