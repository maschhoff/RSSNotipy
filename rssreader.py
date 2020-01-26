"""

RSS Notipy

RSS Reader Plugin for xrel

2020 maschhoff github.com/maschhoff


"""

import requests
import feedparser

def getRSSTitles(url):
    feed = feedparser.parse(url)
    
    #liste=[]
    movie={}
    
    for item in feed["items"]:
        movie[item["title"]]=item["link"]

    return movie
