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

filters = {"track": ["#lulalivre","#lulasolto", "#lula","#DebateBand",
                         "#AlvaroDias", "#CaboDaciolo", "#CiroGomes",
                         "#CiraoDaMassa","#GeraldoAlckmin", "#Boulos","#GuilhermeBoulos",
                         "#HenriqueMeirelles", "#JairBolsonaro","#Bolsonaro",
                         "#Bolsomito","#MelhorJairSeAcostumando","#MarinaSilva",
                         "#FernandoHaddad", "#ManuelaDavila"]} #replace with the keyword that you want
r = api.request('statuses/filter', filters).get_iterator()
out = open("tweets_debateband_20180809_03.txt","w")

for item in r:
    itemString = json.dumps(item)
    out.write(itemString + '\n')
