# send a tweet with a custom message
# ref: https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update

import tweepy
import sys
import os
import subprocess
import time


# twitter api setup
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
 
api.update_status(status='Hello World from Copilot !!!')