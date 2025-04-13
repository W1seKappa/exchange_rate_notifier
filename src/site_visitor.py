import requests


class SiteVisitor:
    def __init__(self, url):
        self.url = url

    def getHtml(self):
        headers = {
            'user-agent': 'Mozilla/5.0',
            # Убираем 'accept-encoding' — requests сам всё сделает
        }
        request = requests.get(self.url, headers=headers)
        return request.text
