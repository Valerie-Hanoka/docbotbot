#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
classify_tweets.py is part of the project docbotbot
Author: Valérie Hanoka

"""

import glob
import json
import ..docdocbot
from .crap_nlp.crap_ner import get_ners

from flair.data import Sentence

def get_tweet_textual_content(json_tweet):
    text = json_tweet['full_text']
    get_ners(text)


for json_tweet in glob.glob('/Users/val/dev/docbotbot/crawled_corpus/*.json'):
    with open(json_tweet) as json_data:
        d = json.load(json_data)
        get_tweet_textual_content(d)
