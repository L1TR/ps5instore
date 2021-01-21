from bs4 import BeautifulSoup
from common.loader import DataLoader
from webdriverdownloader import GeckoDriverDownloader
from selenium import webdriver


class QueueItChecker(object):
    def __init__(self):
        self.url = "https://direct.playstation.com/en-us/ps5"
        self.loader = DataLoader()
        # self.initDriver()

    def initDriver(self):
        gdd = GeckoDriverDownloader()
        gdd.download_and_install()

    def checkQueue(self):
        if not webdriver:
            self.initDriver()
        # browser = webdriver.Firefox()
        browser = webdriver.Firefox(executable_path="/assets/selenium/geckodriver")
        browser.get(self.url)
        # content = self.loader.load(url=self.url)
        # print(content)
        # soup = BeautifulSoup(content, 'html.parser')
        # to_cart_btn = soup.findAll("span", {"class": "product-price"})
        return False
