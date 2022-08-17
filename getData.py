import requests
import re
import glob
from bs4 import BeautifulSoup

array = [
    "http://blog.livedoor.jp/kokon55/archives/1078683714.html",
    "https://h616r825.livedoor.blog/archives/55271096.html",
    "https://h616r825.livedoor.blog/archives/55229217.html",
    "https://h616r825.livedoor.blog/archives/48227185.html",
    "https://h616r825.livedoor.blog/archives/55164278.html",
    "https://h616r825.livedoor.blog/archives/48031465.html",
    "https://h616r825.livedoor.blog/archives/55044532.html",
    "https://h616r825.livedoor.blog/archives/54956930.html",
    "https://h616r825.livedoor.blog/archives/54646470.html",
    "https://h616r825.livedoor.blog/archives/54480245.html",
    "https://h616r825.livedoor.blog/archives/40982880.html",
    "https://h616r825.livedoor.blog/archives/45301878.html"
    ]

def scrape(id,i):
    print("======>"+str(id))
    ss_url = "http://blog.livedoor.jp/kokon55/archives/"+str(id)+".html"

    r = requests.get(ss_url)
    soup = BeautifulSoup(r.text,'lxml')
    ss_containers = soup.find_all('dd')
    ss_text = ""
    for container in ss_containers:
        ss_text += container.get_text()
        ss_text = re.sub("[ 　]","\n",ss_text)
    print(ss_text)
    with open("dataset/nanasaki_ss"+str(i)+".txt", 'w')as f:
        f.write(ss_text)

for i in range(len(array)):
    scrape(array[i],i)
