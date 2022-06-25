# Spotify-Lyrics
find song I'm listening to and give lyrics from genius

Summary:
- Uses spotify API to find the song Im currently listening to
- Uses Genius API to see if a lyric page exists for the song
- Uses a scraper to scrape lyrics from genius lyrics page and stores them in a file which is searched if looking for lyrics
- Uses Tkinter to create a display which consists of:
   - Small button which opens the lyric page for the current song
   - A draggable lyric window which displays lyrics
   - Both windows stay topmost 

Areas Which could be Improved:
- adjust caching file to store the next song in queue aswell
- adjust caching so it is not of unlimited size (currently don't listen to music for very long so not a pressing issue)
