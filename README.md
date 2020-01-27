# RSS Notipy

RSS Notipy is a search and notification service build in python.
It will let you configure movies sources to let you get notipyed when the movie is out on dvd.

![Wish list](https://i.ibb.co/ynrnt56/1.png)
![Movies](https://i.ibb.co/MNfhBVJ/2.png)

# Install and run

` python3 -m pip install -r requirements.txt`
` python3 rss.py`

## Run as docker
` docker pull knex666/rssnotipy`

* volume mount you configuration to /RSSNotipy/data
* use start.sh as entrypoint

# Sample Configuration


```json
{
    "port":3247, 
    "updatetime":1800, 
    "requester":["Harald","Ilse"], 
    "quality":["720p","1080p","2160p"], 
    "date":["2017","2018","2019","2020","2021","2022"],
    "rss":{   
        "Moviepilot.de DVD":"http://rss.filmstarts.de/fs/dvd/baldige", 
        "Filmstarts.de DVD":"http://rss.filmstarts.de/fs/dvd/Neue" 
    }, 
    "movies":{ 
        "Kino.de NEU":"https://www.kino.de/rss/neu-im-kino" 
} 
```


