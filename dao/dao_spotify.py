import os
import random


def spotify_url_song(song):
    song_path = check_url_exists(song)
    if song_path:
        with open(song_path, 'r', encoding='latin-1') as f:
            url_list = [line.strip('\n').split(';')
                        for line in f.readlines()]
        text = show_spotify_links(url_list)
        return text


def check_url_exists(song):
    url_folder = os.path.join(os.getcwd(), 'data/spotify_song_url')
    files = os.listdir(url_folder)
    url_files = [file.split('.')[0] for file in files]
    if song in url_files:
        song_path = os.path.join(url_folder, f"{song}.csv")
        return song_path


def show_spotify_links(url_list):
    choice = random.choice(range(len(url_list)))
    text = f"Listen {url_list[choice][0]} here {url_list[choice][-1]}"
    return text
