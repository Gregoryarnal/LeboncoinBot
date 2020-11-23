import logging

class logger():
    """
    docstring
    """
    log = None
    def __init__(self):
        self.log = logging.basicConfig(filename="bot_leboncoin.log", level=logging.INFO)