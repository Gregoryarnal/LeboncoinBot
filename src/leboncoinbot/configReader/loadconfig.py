import configparser
class loadConfig(object):
    """
    docstring
    """

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.path = config['DATAPATH']['path']
        for elt in config.sections():
            if "ACCOUNT" in elt:
                self.password = config[elt]['password']
                self.username = config[elt]['username']
            if "SCHEDULE" in elt:
                self.schedule = config[elt]['schedule']
