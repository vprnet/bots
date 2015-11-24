#!/usr/local/bin/python2.7

from twython import Twython
from config import consumer_key, consumer_secret, access_token, access_token_secret
from index import new_tweet
import logging

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

try:
    with open("/home/vprnet/webapps/bots/bots/hospital-reports/past_tweets.log", "r") as f:
        reader = f.readlines()
        past_tweets = []

        for row in reader:
            past_tweets.append(row)

        scraped_tweets = new_tweet()

        for report_tweet in scraped_tweets:
            cleaned_tweet = " ".join(report_tweet)

            duplicate = [s for s in past_tweets if cleaned_tweet in s]

            if duplicate:
                print "Already been tweeted."
            else:
                logging.basicConfig(filename="/home/vprnet/webapps/bots/bots/hospital-reports/past_tweets.log", level=logging.INFO)
                logging.info(cleaned_tweet)
                twitter.update_status(status=cleaned_tweet)
                print cleaned_tweet
                print "New tweet tweeted."
except TypeError:
    print "No new hospital reports reported."
