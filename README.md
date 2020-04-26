# RSS Notipy

RSS Notipy is a search and notification service build in python.
It will let you configure movies sources to let you get notipyed when the movie is out on dvd.

You can optionally add the following notification services:
* Pushover (with your APP and User-key)
* Pushbullet (with your API Key)
* openHAB (add the String Item RRSNotipy)

![Wish list](https://i.ibb.co/ynrnt56/1.png)
![Movies](https://i.ibb.co/MNfhBVJ/2.png)

# Install and run

* ` python3 -m pip install -r requirements.txt`
* ` python3 rss.py`

## Run as docker
` docker pull knex666/rssnotipy`

* volume mount you configuration to /RSSNotipy/data
* use start.sh as entrypoint

# Sample Configuration

Please note that all push notification services are optinal and can be empty or left.

```json
{
    "port":3247, 
    "updatetime":1800, 
    "pushbullet_api_key":"Your API Key",
    "pushover_app_token":"Your API Key",
    "pushover_user_key":"Your User Key",
    "openhab_ip":"192.168.100.12 Your openHAB IP",
    "openhab_port":"8080 openHAB port",
    "requester":["Harald","Ilse"], 
    "quality":["720p","1080p","2160p"], 
    "date":["2017","2018","2019","2020","2021","2022"],
    "rss":{   
        "Moviepilot.de DVD":"http://rss.filmstarts.de/fs/dvd/baldige", 
        "Filmstarts.de DVD":"http://rss.filmstarts.de/fs/dvd/Neue" 
    }, 
    "movies":{ 
        "Filmstarts.de NEU":"http://rss.filmstarts.de/fs/kinos/bald?format=xml" 
} 
```

### Test on Repl.it
[![Run on Repl.it](https://repl.it/badge/github/maschhoff/RSSNotipy)](https://repl.it/github/maschhoff/RSSNotipy)