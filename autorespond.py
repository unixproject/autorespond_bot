#import tweepy
#import random
#import time
import tweepy, time, sys, random

CONSUMER_KEY = 'hlYXOClCsMQHpexVaPaXWq0zb'
CONSUMER_SECRET = 'WZYuIfVL25lo5IySnbM8CmzYN3EeDqKWjt3QbWnLDCzlzJT1x0'
ACCESS_TOKEN = '945842581010833409-oAI2Hip01w7rG4IZEaUHqFh6KcTcCyr'
ACCESS_TOKEN_SECRET = '1M3xXM1fBRnnfNgq0laN5QvmPw1EgUfw6AyBzsnyNHAck'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

search_results = api.search(q="groyper", count=1)
 
senteces = ['bbq', 'groyper live matters', 'we are frens', 'stay cozy fren']

for s in search_results:
        message = random.choice(senteces)
        sn = s.user.screen_name
        m = "@%s " % (sn) + str(message)
        s = api.update_status(m, s.id)
sleep(10800)
