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

import csv
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url ="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0"

res= requests.get(url)
res.raise_for_status()
soup=BeautifulSoup(res.text, "lxml")

list_rows=soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
data=[]

x=[]
y=[]

for i in list_rows:
    columns=i.find_all("td")
    if len(columns)<=1:
        continue
    data =[column.get_text().strip() for column in columns]#data를 strip하는게 아니라 x에 써준다
    # list(map(int,data))

    d=(data[2]).split(",")
    d="".join(d)

    data.insert(2,d)
    x.append(data[1])
    y.append(float(data[2]))

print(x)
print(y)
