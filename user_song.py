import json
import requests
from user_info import spotify_user_id
from refersher import Refresh
data = []
data2 = ['Crush', 'Tessa Violet']

class FindSong:
    def __init__(self):
        self.user_id = spotify_user_id
        self.spotify_token = ""

    def current_song(self):
        '''
        find song user is currently playing
        '''
        print("finding song details")
        data = []

        query = "https://api.spotify.com/v1/me/player/currently-playing"

        response = requests.get(query,
                                headers={"Accept": "application/json",
                                        "Content-Type": "application/json",
                                        "Authorization": "Bearer {}".format(self.spotify_token)})
        try:
            response_json = response.json()
        except json.decoder.JSONDecodeError as e:
            print("no song being played or private mode on")
        else:
            try:
                data.append(response_json["item"]["name"])
                for i in response_json["item"]["artists"]:
                    data.append(i["name"])
            except TypeError as t:
                print("ad playing")
        return(data)

    def call_refresh(self):
        '''
        over time token expires so this allows me to access spotify api at anytime even after 30min expiry
        '''
        print("refreshing token")

        refreshCaller = Refresh()

        self.spotify_token = refreshCaller.refresh()

        return self.current_song()

a = FindSong()
a.call_refresh()

