from bs4 import BeautifulSoup
import requests

class AmazonChecker(object):
    def __init__(self):
        self.url = "https://www.amazon.com/dp/B08JGX61H7/?colid=35HQCEADI9UK9&coliid=I2D7GFEBNNPC0O&ref_=lv_ov_lig_pab"
        # self.loader = DataLoader()
        self.headers = ({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', 
                           'Accept-Language': 'en-US, en;q=0.5'})

    def checkState(self):
        client = requests.session()
        response = client.get(self.url, headers=self.headers)
        # content = self.loader.load(url=self.url)
        # soup = BeautifulSoup(content, 'html.parser')
        # doc = html.fromstring(content)
        # XPATH_AVAILABILITY = '//div[@id ="availability"]//text()'
        # RAW_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY) 
        # AVAILABILITY = ''.join(RAW_AVAILABILITY).strip() if RAW_AVAILABILITY else None
        # to_cart_btn = soup.findAll("input", {"value": "Add to cart"})
        # return to_cart_btn
        return False