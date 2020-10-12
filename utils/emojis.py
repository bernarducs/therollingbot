from random import choice


EMOJIS = [['🎶'], ['🎵'], ['🎵🎶'], ['🎶🎵'], ['🎵🎵'],
          ['🎶🎶'], ['🎼'], ['🎼🎵'], ['🎸'], ['🎸🎼'],
          ['🎹🎸'], ['🎷'], ['🎷🎷'], ['🎷🎸'], ['🎶🎼']]

EMOJIS_WIKI = ['📓', '📔', '📒', '🖊', '✒', '📝', '✏', '🖍']


def get_emoji():
    emoji = str(choice(EMOJIS)[0])
    return emoji


def get_emoji_wiki():
    emoji = str(choice(EMOJIS_WIKI)[0])
    return emoji
