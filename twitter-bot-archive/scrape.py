import requests
import random
import datetime
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

    if random_archive_date[:2] == "01":
        month = "January"
    elif random_archive_date[:2] == "02":
        month = "February"
    elif random_archive_date[:2] == "03":
        month = "March"
    elif random_archive_date[:2] == "04":
        month = "April"
    elif random_archive_date[:2] == "05":
        month = "May"
    elif random_archive_date[:2] == "06":
        month = "June"
    elif random_archive_date[:2] == "07":
        month = "July"
    elif random_archive_date[:2] == "08":
        month = "August"
    elif random_archive_date[:2] == "09":
        month = "September"
    elif random_archive_date[:2] == "10":
        month = "October"
    elif random_archive_date[:2] == "11":
        month = "November"
    else:
        month = "December"

    tweet = month + " " + random_archive_date[3:5] + ", " + "20" + random_archive_date[6:8] + ": " + random_archive_headline.title() + " " + url

    return tweet
