"""

RSS Notipy

RSS Reader Plugin

2020 maschhoff github.com/maschhoff


"""

import requests
import feedparser

def getRSSTitles(url):
    feed = feedparser.parse(url)
    movie={}    
    for item in feed["items"]:
        movie[item["title"]]=item["link"]

    return movie


def getMovieTitles(url):
    feed = feedparser.parse(url)
    return feed["items"]