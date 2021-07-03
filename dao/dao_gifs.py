from random import choice
from twitter_api.twitter_api import conn

api = conn()


def get_gif_path(gif):
    return f"data/gifs/{gif}"


def its_tuesday():
    gifs = ['charlie_watts.gif', 'keith_hat.gif', 'mick_keith_arm.gif',
            'ronnie_serious.gif', 'mick_surprised.gif', 'charlie_cigar.gif',
            'mick_what.gif', 'keith_why.gif', 'keef_eyes.gif',
            'mick_start_me_up.gif', 'mick_jumping.gif', 'mick_msg.gif',
            'mick_looking_at.gif', 'mick_smile.gif', 'mick_philosophy.gif',
            'mick_you_cant_what_you_want.gif'
            ]
    picked = choice(gifs)
    file_path = get_gif_path(picked)
    member_name = picked.split('_')[0].capitalize()
    txt = f"What a week, huh?\n{member_name}, " \
          f"it's ruby Tuesday\n\n#rollingstones"
    return api.update_with_media(file_path, txt)
