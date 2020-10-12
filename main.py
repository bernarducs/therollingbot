from time import sleep
from twitter_api.twitter_api import conn
from dao.dao_lyrics import current_song_and_verse
from dao.dao_wiki import get_wiki_song
from dao.dao_spotify import get_spotify_url
from utils.emojis import get_emoji

api = conn()

while True:

    verse, song, new_song, last_verse = current_song_and_verse()
    if new_song:
        intro_txt = f"Today we'going to play {song}! Check it out! 👅"
        print(intro_txt)
        api.update_status(intro_txt)

    verse_txt = f"{verse} {get_emoji()}"
    print(verse_txt)
    api.update_status(verse_txt)
    sleep(120)

    if last_verse:
        wiki = get_wiki_song(song)
        if wiki:
            song_twt_id = None
            for wk in wiki:
                wiki_txt = f"{'📝'} {wk}"
                print(wiki_txt)
                song_twt = api.update_status(wiki_txt, song_twt_id)
                song_twt_id = song_twt.id
                sleep(120)

        spotify = get_spotify_url(song)
        if spotify:
            print(spotify)
            api.update_status(spotify)
