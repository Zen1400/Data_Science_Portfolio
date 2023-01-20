import pandas as pd
import s3fs
from datetime import datetime
import json
import tweepy


access_key = "hoh5f7uS3BKa0SmpfbNSoxxnD"
access_secret = "gd32OPLdoOC6SPLHvBevSsTd368R2jJsfRy0fYFlhr5FoI4NFG"
consumer_key = "1616511421784723471-t6oaVqKddp7jrDylwb6vFUPMrFtR1N"
consumer_secret = "GE5L5bQFvY32TNvgOXTgcR2wwZi7MLmnKTOvQhIK1mp4k"


# Twitter Authentification

auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# Create the API object

api = tweepy.API(auth)


tweets = api.user_timeline(screen_name = '@elonmusk',
                           count = 200,
                           # extract retweets
                           include_rts = False,
                           # To get the full tweet
                           tweet_mode = 'extended')

print(tweets)
