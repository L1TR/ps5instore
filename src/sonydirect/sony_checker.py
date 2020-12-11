import json
from common.loader import DataLoader

class SonyChecker(object):
    def __init__(self):
        self.ps5_url = "https://api.direct.playstation.com/commercewebservices/ps-direct-us/users/2fccb07dfefe1883c361e133df09f03fc66515930060936ac8a2a556e440b2e8/products/productList?fields=BASIC&productCodes=3005816"
        self.digital_url = "https://api.direct.playstation.com/commercewebservices/ps-direct-us/users/2fccb07dfefe1883c361e133df09f03fc66515930060936ac8a2a556e440b2e8/products/productList?fields=BASIC&productCodes=3005817"
        self.loader = DataLoader()

    def checkState(self, is_digital=True):
        url = self.digital_url if is_digital else self.ps5_url
        content = self.loader.load(url=url)
        try:
            parsed = json.loads(content)
            in_stock = parsed['products'][0]['stock']['stockLevelStatus']
            return (in_stock != 'outOfStock', 'Digital' if is_digital else 'Not digital')
        except:
            # Possible in stock
            return (True, 'Digital' if is_digital else 'Not digital')