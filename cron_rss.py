"""

RSS Notipy

RSS Serach Cronjob file

use it with crontab or in a thread every ~ 2h (see config)

2020 maschhoff github.com/maschhoff

"""


import searchfile
import rssreader
import collections
from difflib import SequenceMatcher
import settings
import http.client, urllib

config=settings.loadConfig()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def notifyPushover(movie):
	conn = http.client.HTTPSConnection("api.pushover.net:443")
	conn.request("POST", "/1/messages.json",
	urllib.parse.urlencode({
    "token": config["pushover_app_token"],
    "user": config["pushover_user_key"],
    "message": "New Movie found: "+movie,
  	}), { "Content-type": "application/x-www-form-urlencoded" })
	conn.getresponse()

def run():	
	print("... Running Cron RSS ...")
	search=searchfile.loadSearchfile()

	#Load all entrys from rss resources 
	x_movies={}
	rss=config["rss"]
	for rel in rss:
		x_movies.update(rssreader.getRSSTitles(rss[rel])) # Merge dicts
	

	#Iterate search and rss results
	for film in search:
		#print("Suche nach: "+film["film"])

		for movie, link in x_movies.items():
			#print(movie+"\t"+link)
			#Split on year
			split=movie.split("20")

			#to lowercase without . and spaces
			lmovie=movie.lower()
			lfilm=film["film"].lower()
			lmovie=lmovie.replace(".","")
			lmovie=lmovie.replace(" ","")
			lfilm=lfilm.replace(".","")
			lfilm=lfilm.replace(" ","")

			#result
			gefunden=False

			#method1 - found by substring in string
			if lfilm in lmovie and film["quality"] in movie and film["date"] in movie:
				#print("METHOD1: "+lfilm+"\t"+lmovie)
				gefunden=True

			#method2 - found by similary in percent
			if similar(film["film"],split[0]) > 0.5 and film["quality"] in movie and film["date"] in movie:
				#print("METHOD2: "+movie)
				gefunden=True
			
			
			if gefunden:
				#print("GEFUNDEN: "+movie+"\t"+link)
				#Notify
				if not film["listed"] and config.get("pushover_app_token") is not None or config.get("pushover_app_token")=="":
					notifyPushover(film["film"])

				#Change and save
				film["listed"]=True
				if not link in film["urls"]:
					film["urls"].append(link)
	searchfile.writeSearchfile(search)

#run()
