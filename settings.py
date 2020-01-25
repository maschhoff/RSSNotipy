"""
RSS Notipy

settings - Helpers

2020 maschhoff github.com/maschhoff

"""

import json

def loadConfig():
    #print("loadConfig()")
    res={}
    with open('./data/config.json', 'r') as fp:
        res = json.load(fp)
    return res

#TODO - not used jet
def createConfig(port,updatetime,requester,quality,date,rss):
	data={}
	data["port"]=port
	data["updatetime"]=updatetime
	data["requester"]=requester
	data["quality"]=quality
	data["date"]=date
	data["rss"]=rss

	writeConfig(data)    

def writeConfig(config):
    with open('./data/config.json', 'w') as fp:
	    json.dump(config, fp)