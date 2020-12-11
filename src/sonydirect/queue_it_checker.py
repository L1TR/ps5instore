from bs4 import BeautifulSoup
from common.loader import DataLoader
import requests

class QueueItChecker(object):
    def __init__(self):
        self.url = "https://direct.playstation.com/en-us/ps5"
        self.loader = DataLoader()

    def checkQueue(self):
        content = self.loader.load(url=self.url)
        soup = BeautifulSoup(content, 'html.parser')
        to_cart_btn = soup.findAll("span", {"class": "product-price"})
        return len(to_cart_btn) == 0