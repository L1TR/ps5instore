import json
from common.loader import DataLoader
from common.config import DEFAULT_RETURN_ON_FAULT

class TargetChecker(object):
    def __init__(self):
        self.digital_url = "https://api.target.com/fulfillment_aggregator/v1/fiats/81114596?key=ff457966e64d5e877fdbad070f276d18ecec4a01&nearby=07014-1904&limit=20&requested_quantity=1&radius=75&fulfillment_test_mode=grocery_opu_team_member_test"
        self.ps5_url = "https://api.target.com/fulfillment_aggregator/v1/fiats/81114595?key=ff457966e64d5e877fdbad070f276d18ecec4a01&nearby=07014-1904&limit=20&requested_quantity=1&radius=75&fulfillment_test_mode=grocery_opu_team_member_test"
        self.loader = DataLoader()
        self.notAvailableStatuses = ['OUT_OF_STOCK', 'NOT_SOLD_IN_STORE', 'UNAVAILABLE']

    def checkState(self, is_digital=True):
        url = self.digital_url if is_digital else self.ps5_url
        content = self.loader.load(url=url)
        try:
            parsed = json.loads(content)
            locations = parsed['products'][0]['locations']
            in_stock = any(x['location_available_to_promise_quantity'] > 0 or x['in_store_only']['availability_status'] not in self.notAvailableStatuses or x['order_pickup']['availability_status'] not in self.notAvailableStatuses for x in locations)
            return (in_stock, 'Digital' if is_digital else 'Not digital')
        except:
            # Possible in stock
            return (DEFAULT_RETURN_ON_FAULT, 'Digital' if is_digital else 'Not digital')