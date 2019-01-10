#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
core.py is part of the project docbotbot
Author: Valérie Hanoka

"""

import glob
import json
from docdocbot.crap_nlp.tweet import Tweet
from gensim import corpora
from gensim.models import FastText


def corpus(location = "docdocbot/fetch/crawled_corpus/*.json"):
    for json_tweet_file in glob.glob(location):
        with open(json_tweet_file, 'r') as json_tweet:
            json_tweet = json.loads(json_tweet.read())
            tweet = Tweet(json_tweet)
            yield list(tweet.content_words)


import ipdb; ipdb.set_trace()

corpus = list(corpus())
len(corpus)

ft_model = FastText(min_count=2)
ft_model.build_vocab(sentences=corpus)
#ft_model.train(corpus, total_examples=ft_model.corpus_count, epochs=ft_model.iter)


