class proxies(object):
    """
    docstring
    """
    proxies_dict = {}
    proxies_tab = []
    seek = 0
    def __init__(self):
        with open("ProxyList.txt") as file:
            for proxie in file:
                self.proxies_tab.append(proxie[:-1])

    def get_proxies(self):
        proxie = self.proxies_tab[self.seek]
        self.proxies_dict["http"] = "http://"+proxie
        self.proxies_dict["https"] = "https://"+proxie
        self.seek += 1
        return self.proxies_dict

    def get_proxies_tab(self):
        return self.proxies_tab