import csv
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url ="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=2"

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
    data =[column.get_text().strip() for column in columns]

    d=(data[4]).split(",")
    d="".join(d)

    data.insert(4,d)
    x.append(data[1])
    y.append(data[4])

print(x)
print(y)

plt.rc("font",family="Malgun Gothic")
plt.plot(x,y)
plt.show()