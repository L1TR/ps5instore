import json
from common.loader import DataLoader
from common.config import DEFAULT_RETURN_ON_FAULT


class GameStopChecker(object):
    def __init__(self):
        self.digital_url = "https://www.gamestop.com/on/demandware.store/Sites-gamestop-us-Site/default/Stores-FindStores?hasCondition=true&hasVariantsAvailableForLookup=true&hasVariantsAvailableForPickup=true&source=pdp&showMap=false&products=225171%3a1&postalCode=07029&radius=100"
        self.ps5_url = "https://www.gamestop.com/on/demandware.store/Sites-gamestop-us-Site/default/Stores-FindStores?hasCondition=true&hasVariantsAvailableForLookup=true&hasVariantsAvailableForPickup=true&source=pdp&showMap=false&products=225169%3a1&postalCode=07029&radius=100"
        self.loader = DataLoader()

    def checkState(self, is_digital=True):
        url = self.digital_url if is_digital else self.ps5_url
        content = self.loader.load(url=url)
        try:
            parsed = json.loads(content)
            stores = parsed['stores']
            return (len(stores) > 0, 'Digital' if is_digital else 'Not digital')
        except:
            # Possible in stock
            return (DEFAULT_RETURN_ON_FAULT, 'Digital' if is_digital else 'Not digital')