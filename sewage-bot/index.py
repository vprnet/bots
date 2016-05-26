#!/usr/local/bin/python2.7

import csv

def new_tweet():
    with open("/home/vprnet/webapps/bots/bots/sewage-bot/sewage.csv", "r") as f:
        reader = csv.reader(f)
        all_incidents = []
        new_tweets = []

        for row in reader:
            all_incidents.append(row)

        for line in all_incidents:
            try:
                if line[0] == "Public Alert":
                    tweet_text = line[0] + ": " + line[2] + ", " + line[5]
                    new_tweets.append(tweet_text)
                else:
                    tweet_text = line[0] + ": " + line[5] + ", " + line[2] + ", " + line[4] + ", " + line[6] + ", " + line[9]
                    new_tweets.append(tweet_text)
            except IndexError:
                tweet_text = False

        return new_tweets
