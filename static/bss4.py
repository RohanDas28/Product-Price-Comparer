from bs4 import BeautifulSoup
import requests

url  = "https://www.amazon.in/s?k=watch&ref=nb_sb_noss_1"

r = requests.get(url)

contentt = (r.content)

soup = BeautifulSoup(contentt,"html5lib")
#  a-color-base a-text-normal

txt = soup
# 

cls = txt.find_all("div",class_="s-result-item")
k = (cls.find_all("div",class_="sg-col-inner"))
l = (k.find_all("div",class_="s-expand-height"))




print(l)
