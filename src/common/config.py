import os
from common.consts import Stores

stores_from_env = os.getenv('STORES_TO_CHECK', None)
STORES_TO_CHECK = [Stores(int(v)) for v in stores_from_env.split(",")] if stores_from_env else [Stores.Sony, Stores.Walmart, Stores.Target, Stores.GameStop, Stores.BestBuy]

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', "")
TELEGRAM_CHATID = os.getenv('TELEGRAM_CHATID', "")

BESTBUY_DEVKEY = os.getenv('BESTBUY_DEVKEY', "")

return_on_fault_env = os.getenv('DEFAULT_RETURN_ON_FAULT', False)
DEFAULT_RETURN_ON_FAULT = return_on_fault_env == "True" or return_on_fault_env == True
