#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
crap_tokenisation is part of the project docbotbot
Author: Valérie Hanoka

"""
import regex as re
from docdocbot.crap_nlp.const import (
    SENT_SEP,
    TOK_SEP,
    STOP_WORDS
)

##############################
#    TEXT SEGMENTATION      #
##############################


def segment_tweet(tweet):
    """ Splits a Tweet in tokens and sentences."""

    tokenized_tweet = split_in_tokens(tweet)
    sentencized_tweet = split_in_sentences(tokenized_tweet).strip(SENT_SEP)
    for s in sentencized_tweet.split(SENT_SEP):
        yield s.strip(TOK_SEP).split(TOK_SEP)


def split_in_sentences(tweet):
    """Splits a tokenized Tweet in sentences."""

    sentencified_tweet = ""
    punct = re.finditer(r"%s(\p{P}(?<![\-’#'«»,/()@//]))+%s" % (TOK_SEP, TOK_SEP), tweet)
    start = 0
    for match in punct:
        _, new_start = match.span()
        sentencified_tweet = "%s%s%s" % (
            sentencified_tweet,
            SENT_SEP,
            tweet[start: new_start]
        )
        start = new_start

    if start < len(tweet):
        sentencified_tweet = "%s%s%s" % (
            sentencified_tweet,
            SENT_SEP,
            tweet[start:]
        )
    return sentencified_tweet

def split_in_tokens(tweet):
    """
    Splits a Tweet in tokens, not splitting some Twitter specific
    elements (@, hasthtags, url).
    """

    tokenized_tweet = ""
    splits = re.finditer(r"\s*([\p{P} ]+\s*)", tweet)
    start = 0

    for split in splits:
        end, new_start = split.span()
        tokenized_tweet += " %s %s " % (tweet[start:end], tweet[end: new_start])
        start = new_start
    if start < len(tweet):
        tokenized_tweet += " %s " % tweet[start:]
    tokenized_tweet = re.sub(r'\s+', TOK_SEP, tokenized_tweet)

    # Regrouping hashtags, mentions and urls
    tokenized_tweet = re.sub(r'#%s+' % TOK_SEP, '#', tokenized_tweet)
    tokenized_tweet = re.sub(r'@%s+' % TOK_SEP, '@', tokenized_tweet)
    urls = re.finditer(r'(?P<url>http[%s_:/\.A-Za-z0-9]*)' % TOK_SEP, tokenized_tweet)
    for matched_url in urls:
        tokenized_url = matched_url.group()
        untokenized_url = re.sub(r'%s+' % TOK_SEP, '', tokenized_url)
        tokenized_tweet = re.sub(tokenized_url, untokenized_url, tokenized_tweet)

    return tokenized_tweet

############################
#  STOP-WORDS PROCESSING   #
############################

def is_contentword(word):
    punct = re.fullmatch(r"\p{P}+", word)
    return not (punct or word.lower() in STOP_WORDS)

def get_contentwords(segmented_tweet):
    """ Remove stopwords from a segmented Tweet and lowercase all the tokens."""
    for sent in segmented_tweet:
        tokenized_sent = [tok.lower() for tok in sent if is_contentword(tok)]
        if tokenized_sent:
            yield tokenized_sent
