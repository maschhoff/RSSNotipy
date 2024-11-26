"""

RSS Notipy

Main Server File

2020 maschhoff github.com/maschhoff

"""

import os
from flask import Flask, render_template, request
import logging
import time
import threading
import rssreader
import searchfile
import cron_rss
import settings

app = Flask(__name__)
global config
config=settings.loadConfig()

@app.route('/')
def index():
	search=searchfile.loadSearchfile()
	return render_template('liste.html', config=config, movies=search)

@app.route('/rel/<string:title>')
def rel(title):
	rss=config["rss"]
	url=rss[title]
	movies=rssreader.getRSSTitles(url)
	return render_template('relsource.html', config=config, source=title, movies=movies)


@app.route('/movies/<string:title>')
def movies(title):
	rss=config["movies"]
	url=rss[title]
	movies=rssreader.getMovieTitles(url)
	return render_template('movies.html', config=config, source=title, movies=movies)

#TODO - not implemented jet
"""
@app.route('/<string:search>')
def search(search):
	movies=rssreader.getRSSTitles("")
	res = [i for i in movies if search in i]
	return render_template('relsource.html', source="", movies=movies)    
"""
	

@app.route('/details/<string:id>')
def detailsData(id):
	search=searchfile.loadSearchfile()
	movie=next(item for item in search if item["id"] == id)
	return render_template('details.html', config=config, movie=movie)    


@app.route('/del/<string:id>')
def deleteData(id):
	searchfile.deleteData(id)
	search=searchfile.loadSearchfile()
	return render_template('liste.html', config=config, message="Movie has been deleted" ,movies=search)


@app.route('/refresh')
def refreshing():
	cron_rss.run()
	search=searchfile.loadSearchfile()
	return render_template('liste.html', config=config, movies=search)
	
@app.route('/settings')
def setting():
	config_raw= settings.getConfigRaw()
	return render_template('settings.html', config=config, config_raw=config_raw.read())

@app.route('/settings', methods=['POST'])
def setting_save():
	config_raw=request.form['hiddenconfig']
	settings.writeConfig(config_raw)
	global config
	config=settings.loadConfig()
	#os.execl(sys.executable, sys.executable, *sys.argv)
	return render_template('settings.html', config=config, config_raw=config_raw, message="config saved")

@app.route('/', methods=['POST'])
def my_form_post():
	film = request.form['film']
	if film!="":
		mdate = request.form['date']
		if "any" in mdate:
			mdate=""
		quality = request.form['quality']
		if "any" in quality:
			quality=""
		requester = request.form['requester']
		searchfile.createData(film,mdate,quality,requester,False,[])
	search=searchfile.loadSearchfile()
	if film!="":
		return render_template('liste.html', config=config, message="Movie was added "+film , movies=search)
	else:
		return render_template('liste.html', config=config, message="Error: Movietitle was empty" , movies=search)


def rss_cron():
	while True:
		cron_rss.run()
		time.sleep(config["updatetime"])

if __name__ == '__main__':
	logging.basicConfig(filename='server.log',level=logging.INFO)
	
	#loadConfig
	logging.info("load Config")

	#Cron Thread start
	th = threading.Thread(target=rss_cron)
	logging.info("Starte Cron Thread...")
	th.start()

	#Server start
	logging.info("Start RSS Notipy Server...")
	print("Start RSS Notipy Server...")
	app.run(host='0.0.0.0',port=config["port"],debug=True)

	
