import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=2"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

fluctuations = soup.find_all("span", {"class":"tah"})

for fluctuation in fluctuations:
    print(fluctuation.get_text())



import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
stocks = ['기업은행', '현대글로비스', 'CJ제일제당', '미래에셋증권', 'LG유플러스', '아모레G', '현대중공업지주', '한국금융지주', '한국타이어앤테크놀로지', '현대건설', '강원랜드', '두산중공업', 'SKC', '두산밥캣', '코웨이', '오리온', '한미사이언스', 'LG이노텍', 'GS', '맥쿼리인프라']
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
plt.barh(x,fluctuation,label="등락률",color="b")


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