import re
import pandas as pd
import wikipedia
from wikipedia import WikipediaPage as WP
from utils.scrape_lyrics import get_songs

from spacy.lang.en import English

nlp = English()
nlp.add_pipe(nlp.create_pipe('sentencizer'))


def download_wiki_albums_summary():
    # grab tables from url
    dfs_list = pd.read_html('https://en.wikipedia.org/wiki/The_Rolling_Stones_discography')

    # data frame with albums
    df = dfs_list[1]
    albums_list = [i for i in df['Title']['Title']]

    # drop footnote
    albums_list.pop()
    first_albums = [i[0] for i in re.findall(r"([\w\s\']+) (\w*)",
                                             f"{albums_list[0]}")]
    albums_list.extend(first_albums)
    albums_list.pop(0)

    for album in albums_list:
        summary = wikipedia.summary(f"{album} album")
        album_name_file = re.sub(r"\/?:*|<>'", "", album)
        doc = nlp(summary)
        with open(f"data/wiki/summary/albums/{album_name_file}.txt", 'w', encoding='utf-8') as f:
            for sent in doc.sents:
                f.write(f"{sent.text.strip()}\n")


def download_wiki_lyrics_summary():
    # list of songs with lyrics
    lyrics_songs = get_songs()

    # link's name of page (no matter if song or album links)
    links = WP('List of songs recorded by the Rolling Stones').links

    # wikipedia table with songs and albums
    df = pd.read_html('https://en.wikipedia.org/wiki/List_of_songs_recorded_by_the_Rolling_Stones')[1]

    # cleaning strings
    songs = [s.strip('\/?:*|<>"') for s in df.Title.to_list()]

    # filtering if a link is a song and has lyrics
    links_and_songlyrics = [(x, z) for x in links for y in songs for z in lyrics_songs
                                if y.lower() in x.lower() and z.lower() in y.lower()]

    # saving wikipedia's summary of each song
    for link, song in links_and_songlyrics:
        summary = WP(link).summary
        doc = nlp(summary)
        with open(f"data/wiki/summary/{song}.txt", 'w', encoding='utf-8') as f:
            for sent in doc.sents:
                f.write(f"{sent.text.strip()}\n")
