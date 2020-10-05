from random import choice


EMOJIS = [['🎶'], ['🎵'], ['🎵🎶'], ['🎶🎵'], ['🎵🎵'],
          ['🎶🎶'], ['🎼'], ['🎼🎵'], ['🎸'], ['🎸🎼'],
          ['🎹🎸'], ['🎷'], ['🎷🎷'], ['🎷🎸'], ['🎶🎼']]


def get_emoji():
    emoji = str(choice(EMOJIS)[0])
    return emoji
