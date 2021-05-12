import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=2"

filename = "코스피 인기종목 51~100위.csv"
f = open(filename, "w", encoding="utf8", newline="")
writer = csv.writer(f)

title = "N  종목명 현재가 전일비 등락률 액면가 시가총액    상장주식수   외국인비율   거래량 PER ROE 토론실".split("\t")
writer.writerow(title)

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

<<<<<<< HEAD
data_rows = soup.find("table", attrs = {"class":"type_2"}).find("tbody").find_all("tr")
for row in data_rows:
    columns = row.find_all("td")
    if len(columns) <= 1:
        continue
    data = [column.get_text().strip() for column in columns]
    print(data)
    writer.writerow(data)
=======
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
>>>>>>> d658215369ef7037823424fb8105a1316c6d0362
