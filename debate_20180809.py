# -*- coding: utf-8 -*-
'''
Geting tweets with TwitterAPI
@author: 'Neylson Crepalde'
version: 3.5.2
'''
from twitter_keys import *
from TwitterAPI import TwitterAPI
import json

api = TwitterAPI(consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token_key,
                access_token_secret=access_token_secret)

filters = {"track": ["keyword"]} #replace with the keyword that you want
r = api.request('statuses/filter', filters).get_iterator()
out = open("collected_tweets.txt","w")

for item in r:
    itemString = json.dumps(item)
    out.write(itemString + '\n')
