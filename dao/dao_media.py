import os
from random import choice
from datetime import datetime


def get_album_path(album):
    return f"data/images/{album}"


def get_random_album():
    album_files = os.listdir("data/images")
    album = choice(album_files)
    album_name = album[:-4].capitalize()
    album_path = f"data/images/{album}"
    return album_name, album_path


def album_of_day():
    """
    check if 12am, so send path and name from random album
    by each 5 days
    :return: str, str
    """
    hour = datetime.now().hour
    day_five = datetime.now().day % 5

    if hour == 23 and day_five == 0:
        return get_random_album()
    else:
        return [], []
