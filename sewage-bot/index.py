#!/usr/local/bin/python2.7

import csv

def new_tweet():
    with open('./webapps/bots/bots/sewage-bot/sewage.csv', 'r') as f:
        reader = csv.reader(f)
        all_incidents = []
        new_tweets = []

        for row in reader:
            all_incidents.append(row)

        for line in all_incidents:
            try:
                tweet_text = line[1][:10] + ": " + line[9] + ", " + line[5] + ", " + line[3] + " " + "(" + line[8] + " estimated)"
                new_tweets.append(tweet_text)
            except IndexError:
                tweet_text = False

        return new_tweets
