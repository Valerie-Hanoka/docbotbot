#!/usr/bin/env python# -*- coding: utf-8 -*-"""get_doctoctoc_tweets.py is part of the project docbotbotAuthor: Valérie HanokaUsage: python3 get_doctoctoc_tweets.py -t 3600 -s 7 -d 'tweet_corpus'"""from optparse import OptionParserfrom twython import Twythonimport os.pathimport sysimport timeimport json# Using fish, edit $HOME/.config/fish/config.fish and add corresponding lines# "set -gx DOC_BOT_BOT_CONSUMER_KEY 'mykey'"DOC_BOT_BOT_CONSUMER_KEY = os.environ['DOC_BOT_BOT_CONSUMER_KEY']DOC_BOT_BOT_CONSUMER_SECRET = os.environ['DOC_BOT_BOT_CONSUMER_SECRET']OAUTH_TOKEN = os.environ['TWITTER_OAUTH_TOKEN']OAUTH_TOKEN_SECRET = os.environ['TWITTER_OAUTH_TOKEN_SECRET']twitter = Twython(    DOC_BOT_BOT_CONSUMER_KEY,    DOC_BOT_BOT_CONSUMER_SECRET,    OAUTH_TOKEN,    OAUTH_TOKEN_SECRET)TOTAL_TWEETS_STORED = 0def describe_user(user_info):    """    Returns only the interesting info about the tweet author.    :param user_info: The 'user' dict of a tweet response dict.    :return: a dict with only interesting user info    """    interesting_info = ['screen_name', 'id', 'location', 'description']    return {k: v for k, v in user_info.items() if k in interesting_info}def get_metadata(tweet):    """    Keeps and re-organize a Tweet information    :param tweet: A dict containing all information about a tweet    :return: A dict with filtered information    """    info = {}    info['date'] = time.strptime(tweet.get('created_at'), '%a %b %d %H:%M:%S %z %Y')    info['user'] = describe_user(tweet.get('user'))    # Entities    if tweet['entities']:        ent = tweet['entities']        if ent.get("hashtags"):            info["hashtags"] = [ht.get("text") for ht in ent["hashtags"]]        if ent.get("media"):            info["media"] = [ht.get("expanded_url") for ht in ent["media"]]        if ent.get("urls"):            info["urls"] = [ht.get("urls") for ht in ent["urls"]]    other_interesting_info = [        'full_text',        'retweet_count',        'favorite_count'    ]    info.update({k: v for k, v in tweet.items() if k in other_interesting_info})    return infodef get_tweet(save_to_directory):    global TOTAL_TWEETS_STORED    query = '#doctoctoc -filter:retweets AND -filter:replies'    results = twitter.search(        q=query,        lang='fr',        result_type='recent',        count=100,        tweet_mode="extended"    )    for res in results['statuses']:        filename = res['id']        # If the tweet is already stored, we ignore it        save_to_file = '%s/%i.json' % (            save_to_directory.rstrip('/'),            filename        )        # If the tweet is already stored, we ignore it        # Otherwise, we store it in a JSON file        if not os.path.isfile(save_to_file):            with open(save_to_file, 'w') as outfile:                json.dump(get_metadata(res), outfile)            TOTAL_TWEETS_STORED += 1if __name__ == '__main__':    parser = OptionParser()    parser.add_option("-t", "--total_run_time",                      dest="run_for", default=2,                      help="The total run time of this script")    parser.add_option("-s", "--sleep_time",                      dest="sleep_time", default=5,                      help="Sleep time between requests")    parser.add_option("-d", "--save_to_directory",                      dest="save_to_directory", default='crawled_corpus',                      help="The save directory for all the #DocTocToc tweets")    (options, args) = parser.parse_args()    # Creating the save directory if it does not exist yet    if not os.path.exists(options.save_to_directory):        os.makedirs(options.save_to_directory)    run_for = int(options.run_for)    sleep_time = int(options.sleep_time)    while run_for > 0:        get_tweet(options.save_to_directory)        run_for = run_for - sleep_time        sys.stdout.write(            '{0} minutes remaining, {1} tweet stored.\r'.format(                (int(int(run_for)/60)),                TOTAL_TWEETS_STORED)        )        sys.stdout.flush()        time.sleep(sleep_time)