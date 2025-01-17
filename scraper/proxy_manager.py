import random

class ProxyManager:
    def __init__(self):
        self.proxies = [
            "http://proxy1.example.com:8080",
            "http://proxy2.example.com:8080",
            "http://proxy3.example.com:8080",
        ]

    def get_random_proxy(self):
        return random.choice(self.proxies)
