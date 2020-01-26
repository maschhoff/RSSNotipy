# RSS Notipy

RSS Notipy is a search and notification service build in python.
It will let you configure movies sources to let you get notipyed when the movie is out on dvd.

![Wish list](https://ibb.co/VWsWRDg)
![Movies](https://ibb.co/vzhBXPM)

# Install and run

* python3 -m pip install -r requirements.txt
* python3 rss.py


# Sample Configuration

>{
    "port":3247, #Port http://127.0.0.1:3247 to connect to Notipy
    "updatetime":1800, #Update interval default 2h
    "requester":["Harald","Ilse"], # Requester if you have more than one person interested in dvd
    "quality":["720p","1080p","2160p"], # Quality of the DVD
    "date":["2017","2018","2019","2020","2021","2022"], #Dates to search for
    "rss":{ #List with RSS Release Sources
        "Moviepilot.de DVD":"http://rss.filmstarts.de/fs/dvd/baldige",
        "Filmstarts.de DVD":"http://rss.filmstarts.de/fs/dvd/Neue"
    },
    "movies":{ #List with RSS Movie Information - like IMDB, TMDB;
        "Kino.de NEU":"https://www.kino.de/rss/neu-im-kino"
}



