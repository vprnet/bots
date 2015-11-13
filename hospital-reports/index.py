#!/usr/local/bin/python2.7

import csv

def new_tweet():
    with open('./reports.csv', 'r') as f:
        reader = csv.reader(f)
        new_tweets = []

        for row in reader:
            new_tweets.append(row)

        return new_tweets
