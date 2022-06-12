from configparser import ConfigParser
from os import getcwd, path

import tweepy

tokens_path = path.join(getcwd(), 'twitter_api')
file_path = path.join(tokens_path, 'tokens.ini')

config = ConfigParser()
config.read(file_path)
keys = config['DEFAULT']

CONSUMER_KEY = keys['CONSUMER_KEY']
CONSUMER_SECRET = keys['CONSUMER_SECRET']
ACCESS_TOKEN = keys['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = keys['ACCESS_TOKEN_SECRET']


def conn():

    auth = tweepy.OAuthHandler(
        consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET
    )
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)
