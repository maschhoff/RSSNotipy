"""

RSS Notipy

RSS Reader Plugin for xrel

2020 maschhoff github.com/maschhoff


"""

import requests
from bs4 import BeautifulSoup
import feedparser

def getRSSTitles(url):
    feed = feedparser.parse(url)
    
    #liste=[]
    movie={}
    
    for item in feed["items"]:
        #print(item["title"])
        #print(item["link"])
        movie[item["title"]]=item["link"]
        #liste.append(movie)

    return movie

"""
if __name__ == '__main__':
    print(getRSSTitles("https://www.xrel.to/feeds/atom/releases.xml"))

"""

#https://www.xrel.to/feeds/atom/releases.xml
#https://www.xrel.to/feeds/atom/releases-movie-topmovie.xml'
#https://fileleechers.info/board/forum/index.php?board-feed/819/&at=8048-af1e897cd2b5bd61600abfc71bb8237e88bfa793'