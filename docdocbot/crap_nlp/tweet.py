#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tweet.py is part of the project docbotbot
Author: Valérie Hanoka

"""

from docdocbot.crap_nlp.crap_ner import get_ners
from docdocbot.crap_nlp.crap_tokenisation import (
    segment_tweet,
    get_contentwords
)


class Tweet(object):

    def __init__(self, *args):
        """Represents a DocTocToc Tweet and the relevant information about it."""
        self.__dict__.update(*args)
        self._nl_process()

    def _nl_process(self):
        """ Apply NLP to this Tweet"""
        self.segmented_text = segment_tweet(self.full_text)
        self.named_entities = get_ners(self.full_text)
        self.content_words = get_contentwords(self.segmented_text)
        #import ipdb; ipdb.set_trace()
