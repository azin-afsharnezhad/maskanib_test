
import requests


class TSETMCCrawler:
    __address = 'https://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceDailyList/14079693677610396/0'
    __attrs = {
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        },
    }

    def __init__(self):
        self.__raw_data = None

    def crawl(self) -> dict:
        try:
            if self.__raw_data is None:
                response = requests.get(
                    url=self.__address, headers=self.__attrs['headers'])
                self.__raw_data = response.text.split('},{')
            result = {}
            for item in self.__raw_data:
                result['date'] = item.split('dEven":')[1].split(',')[0]
                result['count'] = int(item.split(
                    'zTotTran":')[1].split('.')[0])
                result['volume'] = float(
                    item.split('qTotTran5J":')[1].split('.')[0])
                result['value'] = float(
                    item.split('qTotCap":')[1].split('.')[0])
                result['yesterday_price'] = int(item.split(
                    'priceYesterday":')[1].split('.')[0])
                result['first_price'] = int(item.split(
                    'priceFirst":')[1].split('.')[0])
                result['last_trade'] = int(
                    item.split('pDrCotVal":')[1].split('.')[0])
                result['close'] = int(item.split(
                    'pClosing":')[1].split('.')[0])
                result['low'] = int(item.split('priceMin":')[1].split('.')[0])
                result['high'] = int(item.split('priceMax":')[1].split('.')[0])
                yield result
        except Exception as error:
            raise Exception(
                f'Unexcepted error in crawling process ... \n {error = }')
