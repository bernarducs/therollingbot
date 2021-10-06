from itertools import zip_longest, filterfalse
from ast import literal_eval
from utils.scrape_lyrics import get_songs

FILE_PATH = 'log/log.txt'


def read_log():
    """
    just reads the log with song and verse number
    :return: str, int
    """
    with open(FILE_PATH, 'r') as file_in:
        log = literal_eval(file_in.read())
    return log['song'], log['verse_number']


def write_log(song, verse_number, last_verse):
    """
        writes a log with a song, verse number and
        if it is last verse
        :return: str, int, bool
        """
    if last_verse:
        song = pick_a_song()
        verse_number = 0
    else:
        verse_number += 1

    dic = {'song': song, 'verse_number': verse_number}
    result = str(dic)
    with open(FILE_PATH, 'w') as file_out:
        file_out.write(result)
    return result


def song_and_verse():
    """
    get current song, verse and if is a new song or last verse
    after, update its status writing a log txt file
    :return: str, str, bool, bool
    """
    first_verse, last_verse = False, False

    song, verse_number = read_log()
    verses = get_verses(song)
    verse = verses[verse_number]

    # check if is it either first or last verse
    if verse_number == 0:
        first_verse = True
    elif verse_number == len(verses) - 1:
        last_verse = True

    write_log(song, verse_number, last_verse)
    return verse, song, first_verse, last_verse


def current_song_and_verse():
    """
    deprecated
    """
    first_verse, last_verse = False, False
    with open('log/log.txt', 'r') as file_in:
        log = eval(file_in.read())
    song, verse_number = log['song'], log['verse_number']
    try:
        verses = get_verses(song)
        verse = verses[verse_number]
        verse_number += 1
        if verse_number == len(verses):
            last_verse = True
        return verse, song, first_verse, last_verse
    except IndexError:
        first_verse = True
        song = pick_a_song()
        verses = get_verses(song)
        verse_number = 0
        verse = None
        return verse, song, first_verse, last_verse
    finally:
        dic = {'song': song, 'verse_number': verse_number}
        with open('log/log.txt', 'w') as file_out:
            file_out.write(str(dic))


def pick_a_song():
    """
    pick a random song from a song's list
    :return: str
    """
    songs = get_songs(shuffled=True)
    return songs[0]


def get_verses(song):
    """
    take all the song divided into verses
    :param song:
    :return: list
    """
    with open("data/lyrics/{}.txt".format(song), "r") as f:
        lines = f.readlines()
        lyrics = [line.strip('\n') for line in lines]

    idx = [0] + [i for i, line in enumerate(lyrics) if len(line) == 0]
    parts = [lyrics[i:j] for i, j in zip_longest(idx, idx[1:])]
    verses = [list(filterfalse(lambda x: len(x) == 0, part)) for part in parts]

    parsed = transform_verses(verses)
    return parsed


def transform_verses(verses):
    """
    take a song's text and put into list with verses
    :param verses:
    :return:
    """
    parsed = list()

    def func(v):
        return ['\n'.join(v[i:i + 2]) for i in range(0, len(v), 2)]

    for verse in verses:
        n_items = len(verse)
        if n_items % 2 == 0:
            parsed.extend(func(verse))
        else:
            first, last = verse[:-3], verse[-3:]
            parsed.extend(func(first))
            parsed.extend(['\n'.join(last)])

    parsed_clean = list(filter(None, parsed))
    return parsed_clean
