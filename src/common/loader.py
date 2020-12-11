import requests


class DataLoader(object):
    def __init__(self, url=None):
        self.url = url
        self.html_content = None
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
            }
        self.params = (
            ('_encoding', 'UTF8'),
            ('type', 'wishlist'),
        )

    def load(self, url=None, cookies={}):
        response = requests.get(url or self.url, headers=self.headers, cookies=cookies)
        return response.text

    def parse(self):
        pass

def main():
    print("Test")
    