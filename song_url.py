import json
import requests
from Genius_data import cs, ci ,uri, at
from user_song import a
from refersher import Refresh

links = []

class Searchin():
    def __init__(self):
        self.at = at

    def search(self):
        '''
        takes data from mainer to search genius for the song url
        '''
        links=[]
        data = a.call_refresh()
        check = open("History", "r")
        current_song = check.read()
        check.close()
        datum = current_song.split("@#$")[0]
        if datum == data:
            return [data, current_song.split("@#$")[1]]
        print(data)
        if len(data) != 0:
            print("searching")
            song_name = data[0]
            song_name = song_name.replace(" ", "%20")
            query = "http://api.genius.com/search?q={0} {1}".format(song_name, data[1])
            response = requests.get(query,
                                    headers={"Authorization": "Bearer {}".format(at)})
            res_json = response.json()
            test = res_json["response"]["hits"]
            for i in test:
                if i["result"]["primary_artist"]["name"] == data[1]:
                    links.append(i["result"]["url"])
        print(links, "links")
        links.append("")
        info = [data, links[0]]
        return info




s = Searchin()
s.search()

