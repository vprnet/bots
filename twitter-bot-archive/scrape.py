#!/usr/local/bin/python2.7

import requests
import random
import datetime
import calendar
from BeautifulSoup import BeautifulSoup

def new_archive_tweet():
    slug = random.randint(74271, 98141)
    random_story = str(slug)

    url = "http://www.vpr.net/news_detail/" + random_story
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)

    headline = soup.find("h2")
    story_date = soup.find("h4")

    random_archive_headline = headline.text
    random_archive_date = story_date.text[:8]

    month = calendar.month_name[int(random_archive_date[:2])]

    tweet = month + " " + random_archive_date[3:5] + ", " + "20" + random_archive_date[6:8] + ": " + random_archive_headline.title() + " " + url

    return tweet
