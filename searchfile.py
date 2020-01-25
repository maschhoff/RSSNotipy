"""
RSS Notipy

searchfile - Helper

Helps to append, delete a movie from a json file.

2020 maschhoff github.com/maschhoff

"""

import json
import random 


def deleteData(id):
	#print("deleteData()")
	search=loadSearchfile()
	i=0
	for s in search:
		if str(id) in s["id"]:
			search.pop(i)
		i+=1
	writeSearchfile(search)
	
	

def createData(film,date,quality,request,listed,urls):
	#print("createData()")
	try:
		search=loadSearchfile()
	except FileNotFoundError as e:
		search=[]
	
	
	data={}
	data["id"]=str(random.randint(0, 100000))
	data["film"]=film
	data["date"]=date
	data["quality"]=quality
	data["request"]=request
	data["listed"]=listed
	data["urls"]=urls
	
	search.append(data)
	writeSearchfile(search)

def loadSearchfile():
	#print("loadSearchfile()")
	res=[]
	try:
		with open('./data/searchfile.json', 'r') as fp:
			res = json.load(fp)
	except:
		print("Seachfile empty")
	#print(str(res))
	return res


def writeSearchfile(search):
	#print("writeSearchfile()")
	with open('./data/searchfile.json', 'w') as fp:
		json.dump(search, fp)
		
	
	

#createData("Rambo","2019","1080p","Matze",False,None)
#search=loadSearchfile()
#print(search[1]["film"])
#deleteData(94688)