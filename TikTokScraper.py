import requests
from bs4 import BeautifulSoup
import json

content = requests.get("https://tikrank.com/tiktok-influencer-rank/top-100-influencer-in-tiktok-sorted-by-fans-weekly").content
soup = BeautifulSoup(content,"lxml")
links = []

for a in soup.findAll("a",attrs={"class":"dashboard__user__name"}):
    links.append(a['href'])

outfile = open("Top_100_TikTok_Influencers.json","a")
for link in links:
    print(link)
    content = BeautifulSoup(requests.get("https://www.tikrank.com{}".format(link)).content,"lxml")
    outfile.write(content.text)
    outfile.write(",\n")

outfile.close()
