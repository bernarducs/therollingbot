from math import ceil
import pandas as pd
from wikipedia import WikipediaPage as WP
from scrape_lyrics import get_songs

import spacy  # noqa
from spacy.lang.en import English

nlp = English()
nlp.add_pipe(nlp.create_pipe('sentencizer'))


def summary_tweets(song):
    pass


def download_wiki_summary():
    # list of songs with lyrics
    lyrics_songs = get_songs()

    # link's name of page (no matter if song or album links)
    links = WP('List of songs recorded by the Rolling Stones').links

    # wikipedia table with songs and albums
    df = pd.read_html('https://en.wikipedia.org/wiki/List_of_songs_recorded_by_the_Rolling_Stones')[1]

    # cleaning strings
    songs = [s.strip('\/?:*|<>"') for s in df.Title.to_list()]
    albums = [a.strip('\/?:*|<>"') for a in df['Original release'].to_list()]

    # filtering if a link is a song and has lyrics
    links_and_songlyrics = [(x, z) for x in links for y in songs for z in lyrics_songs
                                if y.lower() in x.lower() and z.lower() in y.lower()]

    # saving wikipedia's summary of each song
    for link, song in links_and_songlyrics:
        summary = WP(link).summary
        doc = nlp(summary)
        with open(f"wiki\\summary\\{song}.txt", 'w', encoding='utf-8') as f:
            for sent in doc.sents:
                f.write(f"{sent.text.strip()}\n")
