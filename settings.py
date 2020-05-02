"""
RSS Notipy

settings - Helpers

2020 maschhoff github.com/maschhoff

"""

import json

def getConfigRaw():
	config_raw= open('./data/config.json', 'r')
	return config_raw

def loadConfig():
    #print("loadConfig()")
    res={}
    with open('./data/config.json', 'r') as fp:
        res = json.load(fp)
    return res
   

def writeConfig(config):
	f = open("./data/config.json", "w")
	f.write(config)
	f.close()