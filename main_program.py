import requests
from bs4 import BeautifulSoup
import os

url="http://www.python.org"
headers={"User-Agent":"Mozilla/5.0"}
response=requests.get(url,headers=headers)
html=response.text
soup=BeautifulSoup(html,'html.parser')
body=soup.body
ul=body.find('div',id='touchnav-wrapper')\
    .find('div',id='content')\
    .find('div',class_='container')\
    .find('section',class_='main-content')\
    .find('div',class_='list-widgets row')\
    .find('div',class_='medium-widget blog-widget')\
    .find('div',class_='shrubbery')\
    .find('ul',class_='menu')
lis=[]
for li in ul.find_all('li'):
    a=li.find('a')
    lis.append(a.get_text(strip=True))
if os.path.exists("news_last.txt"):
    with open("news_last.txt","r",encoding="utf-8") as f:
        content=[line.rstrip("\n") for line in f.readlines()]
        if lis==content:
            print("No new updates.")
        else:
            print("News updates available.")
            news=[]
            time=[]
            for li in ul.find_all('li'):
                a = li.find('a')
                text=a.get_text(strip=True)
                if text not in content:
                    news.append(text)
                    time_tag=li.find('time')
                    time.append(time_tag['datetime'][0:10]+' '+time_tag['datetime'][11:16])
            with open("Changelog.txt","a",encoding="utf-8") as f1:
                for i in range(len(news)):
                    f1.write('[')
                    f1.write(time[i])
                    f1.write('] ')
                    f1.write(news[i])
                    f1.write("\n")
else:
    news = []
    time = []
    for li in ul.find_all('li'):
        a = li.find('a')
        text = a.get_text(strip=True)
        news.append(text)
        time_tag = li.find('time')
        time.append(time_tag['datetime'][0:10]+' '+time_tag['datetime'][11:16])
    with open("Changelog.txt", "a", encoding="utf-8") as f1:
        for i in range(len(news)):
            f1.write('[')
            f1.write(time[i])
            f1.write('] ')
            f1.write(news[i])
            f1.write("\n")
with open("news_last.txt","w+",encoding="utf-8") as f:
    for news in lis:
        f.write(news)
        f.write("\n")