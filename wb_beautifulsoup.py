import requests
from bs4 import BeautifulSoup
class wb_beautifulsoup:

    def __init__(self,url,tag,index):
        self.url = url
        self.tag = tag
        self.index = index
        self.price = None
    def get_tether_price(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        tether= soup.find_all(self.tag)[self.index]
        # print("The tether price on "+self.url+" is "+tether.text+"")
        self.price =tether.text

    