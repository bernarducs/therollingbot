from time import sleep

import tweepy

from dao.dao_images import album_of_day
from dao.dao_lyrics import song_and_verse
from dao.dao_spotify import spotify_url_song
from dao.dao_videos import post_video_song
from dao.dao_wiki import wiki_song
from twitter_api.twitter_api import conn
from utils.emojis import get_emoji

api = conn()

while True:

    verse, song, new_song, last_verse = song_and_verse()
    if new_song:
        intro_txt = (
            f"Today we're going to play {song}!\nCheck it out! 👅 "
            f'#rollingstones'
        )
        print(intro_txt)
        api.update_status(intro_txt)
        sleep(60 * 60)

    if verse:
        verse_txt = f'{verse} {get_emoji()}'
        print(verse_txt)
        try:
            api.update_status(verse_txt)
        except tweepy.errors.TweepyException as e:
            print(e)
        sleep(60 * 60 * 3)

    if last_verse:
        wiki = wiki_song(song)
        if wiki:
            song_twt_id = None
            for wk in wiki:
                wiki_txt = f"{'📝'} {wk}"
                print(wiki_txt)
                song_twt = api.update_status(
                    wiki_txt, in_reply_to_status_id=song_twt_id
                )
                song_twt_id = song_twt.id
                sleep(60 * 60)

        spotify = spotify_url_song(song)
        if spotify:
            spfy_txt = f'{spotify} #rollingstones'
            print(spfy_txt)
            api.update_status(spfy_txt)
            sleep(60 * 60)

        post_video_song(song)
        sleep(60 * 60)

        name_album, path_album = album_of_day()
        if name_album:
            print(name_album, path_album)
            api.update_status_with_media(
                status=f'Album of the day 📀 {name_album} #rollingstones',
                filename=path_album,
            )
            sleep(60 * 60 * 3)
