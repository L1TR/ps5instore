import sched, time
from collections import defaultdict
from typing import DefaultDict
from amazon.amazon_checker import AmazonChecker
from sonydirect.sony_checker import SonyChecker
from common.telegram_sender import TelegramSender
from walmart.walmart_checker import WalmartChecker
from target.target_checker import TargetChecker
from gamestop.gamestop_checker import GameStopChecker
from bestbuy.bestbuy_checker import BestBuyChecker
from sonydirect.queue_it_checker import QueueItChecker
from common.config import STORES_TO_CHECK, Stores

IS_DEBUG = False  # __debug__ doesn't work as expected in Docker


class Runner(object):
    """Runner for all store checkers"""
    def __init__(self):
        self.logger = TelegramSender()
        self.amazonChecker = AmazonChecker()
        self.sonyChecker = SonyChecker()
        self.walmartChecker = WalmartChecker()
        self.targetChecker = TargetChecker()
        self.gamestopChecker = GameStopChecker()
        self.bestbuyChecker = BestBuyChecker()
        self.queueItChecker = QueueItChecker()
        self.storeRunMapping = {
            Stores.BestBuy: self.checkBestBuy,
            Stores.Target: self.checkTarget,
            Stores.Walmart: self.checkWalmart,
            Stores.GameStop: self.checkGameStop,
            Stores.Sony: self.checkSony,
            Stores.SonyQueue: self.checkSonyQueue,
            Stores.Amazon: self.checkAmazon
        }
        self.states = defaultdict(bool)

    def checkAmazon(self):
        in_store = self.amazonChecker.checkState()
        if in_store:
            self.logger.send("Amazon. In store: %s" % self.amazonChecker.url)
        else:
            self.logger.send("Amazon. Out of stock")

    def checkState(self, service, serviceName: str, serviceKey: str=None):
        """
        Checks state of the item in the store
        :param service: 
        :param serviceName: name of the store
        :param serviceKey: key for dict self.states
        """
        print("Checking {store}".format(store=serviceName))
        serviceKey = serviceKey or serviceName.lower()
        in_store, adds = service.checkState(is_digital=True)
        if not in_store:
            in_store, adds = service.checkState(is_digital=False)
        if in_store:
            print('Sony. In Stock')
            if not self.states[serviceKey]:
                self.states[serviceKey] = True
                self.logger.send("{store}. In Stock {additional_info}".format(store=serviceName, additional_info=adds))
            else:
                self.states[serviceKey] = False
                msg = "{store}. Out of Stock".format(store=serviceName)
                if IS_DEBUG:
                    self.logger.send(msg)
                print(msg)

    def checkSony(self):
        self.checkState(self.sonyChecker, "Sony")

    def checkWalmart(self):
        self.checkState(self.walmartChecker, "Walmart")

    def checkTarget(self):
        self.checkState(self.targetChecker, "Target")

    def checkGameStop(self):
        self.checkState(self.gamestopChecker, "GameStop")
        
    def checkBestBuy(self):
        self.checkState(self.bestbuyChecker, "BestBuy")

    def checkSonyQueue(self):
        print("Checking Sony Queue")
        is_queue = self.queueItChecker.checkQueue()
        if is_queue:
            if not self.states['queue']:
                self.states['queue'] = True
                self.logger.send("Sony have opened queue")
        else:
            self.states['queue'] = False

    def runCheck(self):
        for store in STORES_TO_CHECK:
            self.storeRunMapping[store]()


def main():
    runner = Runner()
    if IS_DEBUG:
        runner.runCheck()
    else:
        scheduler = sched.scheduler(time.time, time.sleep)

        def run(sc):
            runner.runCheck()
            scheduler.enter(60, 1, run, (sc,))

        scheduler.enter(2, 1, run, (scheduler,))
        scheduler.run()


if __name__ == "__main__":
    main()
