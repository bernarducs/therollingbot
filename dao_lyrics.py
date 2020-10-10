from itertools import zip_longest, filterfalse


def get_verses(song):
    with open("lyrics\\{}.txt".format(song), "r") as f:
        lines = f.readlines()
        lyrics = [line.strip('\n') for line in lines]

    idx = [0] + [i for i, line in enumerate(lyrics) if len(line) == 0]
    parts = [lyrics[i:j] for i, j in zip_longest(idx, idx[1:])]
    verses = [list(filterfalse(lambda x: len(x) == 0, part)) for part in parts]

    parsed = transform_verses(verses)
    return parsed


def transform_verses(verses):
    parsed = list()

    def func(v):
        return ['\n'.join(v[i:i + 2]) for i in range(0, len(v), 2)]

    for verse in verses:
        n_items = len(verse)
        if n_items % 2 == 0:
            parsed.append(func(verse))
        else:
            first, last = verse[:-3], verse[-3:]
            parsed.append(func(first))
            parsed.append(['\n'.join(last)])

    parsed_clean = list(filter(None, parsed))
    return parsed_clean
