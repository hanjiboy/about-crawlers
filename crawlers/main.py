import sys
import getopt

from steps.air import Air
from steps.dcard import DCard
from steps.ophouse import OPHouse
from steps.pchome import PChome
from steps.sinya import SinYa
from steps.stock_ai import StockAi
from steps.yahoo_movie_rank import YMR


def main():
    short_opts = 'hu:'
    long_opts = 'help url='.split()

    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError:
        print('please enter a url')
        sys.exit(2)

    url = ''
    for opt, arg in opts:
        if opt == '-h':
            print('please enter a url')
            sys.exit(2)
        elif opt in ('-u', '--url'):
            url = arg
        else:
            print('please enter a url')
            sys.exit(2)

    if url == 'https://airtw.epa.gov.tw/json/camera_ddl_pic/camera_ddl_pic_2021111112.json?t=1636609462732':
        Air(url)

    elif url == 'https://www.dcard.tw/f/entertainer/p/236972282':
        DCard(url)

    elif url == 'https://www.coolpc.com.tw/evaluate.php':
        OPHouse(url)

    elif url == 'https://ecshweb.pchome.com.tw/search/v3.3/all/results':
        PChome(url)

    elif url == 'https://www.sinya.com.tw/diy/api_prods':
        SinYa(url)

    elif url == 'https://chart.stock-ai.com/history':
        StockAi(url)

    elif url == 'https://movies.yahoo.com.tw/chart.html':
        YMR(url)

    else:
        print('url error')


if __name__ == '__main__':
    main()



