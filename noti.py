"""

RSS Notipy

Notification Services

2020 maschhoff github.com/maschhoff

"""

import http.client, urllib
import requests
import settings
import json

config=settings.loadConfig()
message="New movie found: "

def notifyPushover(movie):
    if config.get("pushover_app_token") is not None and config.get("pushover_app_token")!="":
        conn = http.client.HTTPSConnection("api.pushover.net:443")
        conn.request("POST", "/1/messages.json",
        urllib.parse.urlencode({
        "token": config["pushover_app_token"],
        "user": config["pushover_user_key"],
        "message": message+" "+movie,
        }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()

#Notification to the String-item RSSNotipy
def notifyOpenHAB(movie):
    if config.get("openhab_ip") is not None and config.get("openhab_ip")!="" and config.get("openhab_port") is not None and config.get("openhab_port")!="":
        url = "http://"+config["openhab_ip"]+":"+config["openhab_port"]+"/rest/items/RSSNotipy"
        headers = {'Content-type': 'text/plain'}
        requests.post(url, data=message+" "+movie, headers=headers)

def notifyPushbullet(movie):
    if config.get("pushbullet_api_key") is not None and config.get("pushbullet_api_key")!="":
        data_send = {"type": "note", "title": "RSSNotipy", "body": message+""+movie}
        requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                            headers={'Authorization': 'Bearer ' + config["pushbullet_api_key"], 'Content-Type': 'application/json'})

def notifyAll(movie):
    try:
        notifyPushover(movie)
        notifyPushbullet(movie)
        notifyOpenHAB(movie)
    except:
        print("Error while sending notifications...")

