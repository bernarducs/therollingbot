import re
from random import shuffle

import requests

import lyricwikia as lw
from lyricwikia import LyricsNotFound


def download_songs():
    r = requests.get("https://lyrics.fandom.com/wiki/The_Rolling_Stones")
    songs = re.findall(r'title=\"The Rolling Stones:([\s\w]+)\"\>', r.text)
    # write file
    with open("songs.txt", 'r', encoding="utf-8") as f:
        for song in songs:
            f.write(f"{song}\n")


def get_songs(shuffled=False):
    with open('songs_list\\songs.txt', 'r') as f:
        lines = f.readlines()
        songs = [line.strip('\n') for line in lines]
        if shuffled:
            shuffle(songs)
        return songs


def download_lyrics(songs_list):
    for song in songs_list:
        print(f"Searching for {song} lyrics...")
        try:
            lyrics = lw.get_lyrics('the rolling stones', song)
            with open(f"lyrics\\{song}.txt", 'w', encoding='utf-8') as f:
                f.write(lyrics)
        except LyricsNotFound:
            print("Lyrics not found.")
