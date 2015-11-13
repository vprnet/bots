import random
from config import NPR_API_KEY
from query import api_feed
from scrape import new_archive_tweet
from datetime import date

def new_tweet():
    tags = [178480359]
    story = api_feed(tags, numResults=1)
    today = date.today()

    digital_tweet = (story)[0]['date'] + ": " + (story)[0]['title'] + " " + (story)[0]['link']
    archive_tweet = new_archive_tweet()

    random_tweet = random.randint(1, 2)

    if random_tweet == 1:
        tweet = digital_tweet
    else:
        tweet = archive_tweet

    if date.weekday(today) == 3:
        return tweet + " #tbt"
    else:
        return tweet
