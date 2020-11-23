
import logging
import requests
from configReader.loadconfig import loadConfig
from proxies import proxies
import os
class LeboncoinBot(object):
    """
    docstring
    """
    def __init__(self):
        logging.basicConfig(filename="bot_leboncoin.log", level=logging.INFO)
        logging.info('Start application')
        proxies_generator = proxies()
        config = loadConfig()
        self.load_data(config.path)
        r = requests.get("http://toscrape.com", proxies=proxies_generator.get_proxies())
        while r.status_code != 200:
            try:
                proxie = proxies_generator.get_proxies()
                r = requests.get("http://toscrape.com", proxies=proxie)
            except: 
                logging.error('fail requests')

        print("r" + str(r))

    def load_data(self, path):
        if not os.path.exists(path):
            logging.error('path not exist')
            raise


bot = LeboncoinBot()