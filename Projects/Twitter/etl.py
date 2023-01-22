import pandas as pd
import s3fs
from datetime import datetime
import json
import tweepy


def run_twitter() :
    access_key = "hoh5f7uS3BKa0SmpfbNSoxxnD"
    access_secret = "gd32OPLdoOC6SPLHvBevSsTd368R2jJsfRy0fYFlhr5FoI4NFG"
    consumer_key = "1616511421784723471-t6oaVqKddp7jrDylwb6vFUPMrFtR1N"
    consumer_secret = "GE5L5bQFvY32TNvgOXTgcR2wwZi7MLmnKTOvQhIK1mp4k"


    # Twitter Authentification

    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)

    # Create the API object

    api = tweepy.API(auth)

    # Getting Elon's tweets
    elon_tweets = api.user_timeline(screen_name = '@elonmusk',
                            count = 200,
                            # extract retweets
                            include_rts = False,
                            # To get the full tweet
                            tweet_mode = 'extended')

    l = []
    for tweet in elon_tweets :
        text = tweet._json['full_text']
        refined_tweet = {'user' : tweet.user.screen_name,
                        'text' : text,
                        'favorite_count' : tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at
                        }
        l.append(refined_tweet)


    # Getting Trump's tweets
    trump_tweets = api.user_timeline(screen_name = '@realDonaldTrump',
                            count = 200,
                            # extract retweets
                            include_rts = False,
                            # To get the full tweet
                            tweet_mode = 'extended')


    for tweet in trump_tweets :
        text = tweet._json['full_text']
        refined_tweet = {'user' : tweet.user.screen_name,
                        'text' : text,
                        'favorite_count' : tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at
                        }
        l.append(refined_tweet)

    # Create a Data Frame and save as a csv file in an S3 bucket

    df = pd.DataFrame(l)
    df.to_csv('s3://zein-twitter-t/elon_tweets.csv')
