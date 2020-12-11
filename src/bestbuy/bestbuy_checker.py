import json
from common.loader import DataLoader
from common.config import BESTBUY_DEVKEY, DEFAULT_RETURN_ON_FAULT


class BestBuyChecker(object):
    def __init__(self):
        self.key = BESTBUY_DEVKEY
        self.ps5_url = "https://api.bestbuy.com/v1/products(sku in(6426149,6430161))?format=json&show=inStoreAvailability,onlineAvailability,salePrice&apiKey=%s"%self.key
        self.loader = DataLoader()

    def checkState(self, is_digital=False):
        url = self.ps5_url
        content = self.loader.load(url=url)
        try:
            parsed = json.loads(content)
            in_stock = parsed['products']
            print("BestBuy response: ", in_stock)
            return (any(x['inStoreAvailability'] or x['onlineAvailability'] for x in in_stock), in_stock)
        except:
            # Possible in stock
            print("BestBuy", content)
            return (DEFAULT_RETURN_ON_FAULT, content)