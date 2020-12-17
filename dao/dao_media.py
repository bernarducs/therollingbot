import os
from random import choice
from datetime import datetime as dt
import pandas as pd


def get_album_path(album):
    return f"data/images/{album}"


def get_random_album():
    album_files = os.listdir("data/images")
    album = choice(album_files)
    album_name = album[:-4].capitalize()
    album_path = f"data/images/{album}"
    return album_name, album_path


def album_of_day():
    df = pd.read_csv('data/albums_list/albums.csv', sep=";")

    # today, only month and day
    today = dt.strftime(dt.today(), "%m-%d")
    df_album = df.query("month_day == @today").head(1)

    if df_album.shape[0] != 0:
        album = df_album.album.iloc[0]
        path = df_album.path.iloc[0]
        return album, path
    else:
        album, path = None, None
        return album, path
