from time import sleep
import tweepy
from twitter_api.twitter_api import conn
from dao.dao_lyrics import current_song_and_verse
from dao.dao_wiki import wiki_song
from dao.dao_spotify import spotify_url_song
from dao.dao_media import album_of_day
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
    try:
        api.update_status(verse_txt)
    except tweepy.error.TweepError as e:
        print(e)
    sleep(60 * 60 * 3)

    if last_verse:
        wiki = wiki_song(song)
        if wiki:
            song_twt_id = None
            for wk in wiki:
                wiki_txt = f"{'📝'} {wk}"
                print(wiki_txt)
                song_twt = api.update_status(wiki_txt, song_twt_id)
                song_twt_id = song_twt.id
                sleep(60 * 60)

        spotify = spotify_url_song(song)
        if spotify:
            print(spotify)
            api.update_status(spotify)
            sleep(60 * 60 * 3)

    name_album, path_album = album_of_day()
    if name_album:
        api.update_with_media(path_album, f"{name_album} {'💽💿📀'}")