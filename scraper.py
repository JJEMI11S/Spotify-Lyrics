import requests
from song_url import s
from bs4 import BeautifulSoup
lyrics = "error"
current_song = {}
def lyriccheck():
    info = s.search()
    link = info[1]
    if len(link) > 0:
        if link in current_song:
            return current_song[link]
        r=requests.get(link, headers = { 'User-Agent' : 'Mozilla/5.0' })
        soup = BeautifulSoup(r.text, "html.parser")
        html = soup.prettify("utf-8")
        lyrics = []
        for div in soup.findAll("div", attrs = {"class":"lyrics"}):
            lyrics.append(div.text.strip().split(" "))
            print(lyrics)
        try:
            lyrics = " ".join(lyrics[0])
            current_song[link] = lyrics
            save_file = open("History", "w")
            save_file.write(str(info[0]) + "@#$" + str(info[1]))
            save_file.close()
            return lyrics
        except IndexError:
            return "server not responding, try again later"
    else:
        return "couldn't find song lyrics"
lyriccheck()
