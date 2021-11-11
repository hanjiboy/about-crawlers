import requests
from bs4 import BeautifulSoup
from pprint import pprint


def YMR(url):
    global release_date
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('div', class_='tr')
    colname = list(rows.pop(0).stripped_strings)

    contents = []
    for row in rows:
        thisweek_rank = row.find_next('div', attrs={'class': 'td'})
        updown = thisweek_rank.find_next('div')
        lastweek_rank = updown.find_next('div')

        if thisweek_rank.string == str(1):
            moive_title = lastweek_rank.find_next('h2')
        else:
            moive_title = lastweek_rank.find_next('div', attrs={'class': 'rank_txt'})

        try:
            release_date = moive_title.find_next('div', attrs={'class': 'td'})
            if release_date.string == '未定':
                continue
            trailer = release_date.find_next('div', attrs={'class': 'td'})
            trailer_url = trailer.find('a')['href']
        except TypeError:
            trailer_url = None
        stars = row.find('h6', attrs={'class': 'count'})
        lastweek_rank = lastweek_rank.string if lastweek_rank.string else ''

        c = [thisweek_rank.string, lastweek_rank, moive_title.string, release_date.string, trailer_url, stars.string]
        pprint(c)
