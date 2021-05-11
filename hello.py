import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=2"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

titles = soup.find_all("a", {"class":"tltle"})

for title in titles:
    print(title.get_text())