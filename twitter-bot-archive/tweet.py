#!/usr/local/bin/python2.7

import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret
from index import new_tweet

class TwitterAPI:
    def __init__(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet(new_tweet())
