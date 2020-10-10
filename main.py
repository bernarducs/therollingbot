from time import sleep
from itertools import zip_longest

from scrape_lyrics import get_songs
from dao_lyrics import get_verses
from dao_wiki import get_wiki_song
from dao_spotify import get_spotify_url
from emojis import get_emoji

songs = get_songs(shuffled=True)
for song in songs:
    # intro
    print(f"Today we'going to play {song}. Check it out!\n")

    # verses and wiki
    verses = get_verses(song)
    wikis = get_wiki_song(song)
    for index, (verse, wiki) in enumerate(zip_longest(verses, wikis)):
        # print(song, index)
        print(get_emoji(), verse[0], get_emoji(), '\n')
        sleep(2)
        if wiki:
            print(wiki, '\n')
            sleep(2)

    # spotify
    spotify = get_spotify_url(song)
    print(spotify, '\n')
