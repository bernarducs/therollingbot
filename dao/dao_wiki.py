def wiki_song(song):
    path = 'data/wiki/summary/{}.txt'.format(song)
    try:
        with open(path, 'r', encoding='latin-1') as f:
            lines = f.readlines()
            wiki = [line.strip('\n') for line in lines]
            return wiki
    except FileNotFoundError:
        return []
