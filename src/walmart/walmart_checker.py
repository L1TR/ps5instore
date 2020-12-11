import json
import requests
from requests import cookies


COOKIES_KEY = "TS01ba8c4b"

class WalmartChecker(object):
    def __init__(self):
        self.ps5_url = "https://search.mobile.walmart.com/v1/products-by-code/UPC/711719541028"
        self.digital_url = "https://search.mobile.walmart.com/v1/products-by-code/UPC/711719541035"
        self.cookies = { 
            COOKIES_KEY: "01538efd7c118fe5134c1862a7270941a4fcb5a7f637c75e4c42543076fcf85be653f59fad43c9a52eef0fa106bd69eb8674411723",
            "Path": "/"
        }
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
            }
        self.client = requests.session()

    def checkState(self, is_digital=True):
        url = self.digital_url if is_digital else self.ps5_url
        response = self.client.get(url=url, headers=self.headers, cookies=self.cookies)
        if COOKIES_KEY in response.cookies:
            self.cookies[COOKIES_KEY] = response.cookies[COOKIES_KEY]
        try:
            parsed = json.loads(response.text)
            in_stock = parsed['data']['online']['inventory']['available']
            return (in_stock, 'Digital' if is_digital else 'Not digital')
        except:
            # Possible in stock
            print("Walmart. Error. Response: ", response.text)
            return (True, 'Digital' if is_digital else 'Not digital')