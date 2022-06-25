import requests
from song_url import s
from bs4 import BeautifulSoup
lyrics = "error"
current_song = {}
def lyriccheck():
    '''
    get lyrics of song and stores in lyrics
    '''
    info = s.search()
    link = info[1]
    save_file = open("History", "r")
    for song in save_file.readlines():
        song = song.split("@#$")
        print(song[0])
        print(info[0])
        if str(song[0]) == str(info[0]):
            print("skip")
            return song[1].replace("/n", "\n")
    if len(link) > 0:
        if link in current_song:
            return current_song[link]
        r=requests.get(link, headers = { 'User-Agent' : 'Mozilla/5.0' })
        soup = BeautifulSoup(r.text, "html.parser")
        html = soup.prettify("utf-8")
        lyrics = []

        for div in soup.findAll("div", attrs = {"data-lyrics-container":"true"}):
            test = div.get_text(separator= "\n").strip()

            lyrics.append(test.strip().split(" "))
        try:
            lyrics = " ".join(lyrics[0])
            current_song[link] = lyrics
            save_file = open("History", "a")
            save_file.write(str(info[0]) + "@#$" + str(lyrics.replace('\n', "/n")) + "\n")
            save_file.close()
            return lyrics
        except IndexError:
            return "server not responding, try again later"
    else:
        return "couldn't find song lyrics"
lyriccheck()
