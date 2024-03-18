
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
response = requests.get("https://bitbarg.com/coin/tether")
soup = BeautifulSoup(response.text, "html.parser")
dim= soup.find_all('span')[7]
bitbarg_usdt = dim.text
print(dim.text)








