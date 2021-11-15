import shelve

import tweepy

from twitter_secrets import api_key, api_secret_key

twitter_api = None

def get_twitter_api():
    global twitter_api
    if twitter_api is None:
        auth = tweepy.AppAuthHandler(api_key, api_secret_key)
        twitter_api = tweepy.API(auth)

def generate_twitter_threads(papers):
    # generate twitter threads for papers that have them
    with shelve.open('twitter_threads_cache') as twitter_threads:
        for publication in papers.values():
            if hasattr(publication, 'last_tweet_in_thread'):
                if publication.last_tweet_in_thread in twitter_threads:
                    publication.twitter_thread = twitter_threads[publication.last_tweet_in_thread]
                else:
                    get_twitter_api()
                    i = publication.last_tweet_in_thread
                    tweets = []
                    omit = 0
                    while i is not None:
                        s = twitter_api.get_status(i)
                        embed = twitter_api.get_oembed('https://twitter.com/twitter/statuses/'+s.id_str, hide_thread=1, omit_script=omit, dnt=1, maxwidth=400)
                        tweets.append(embed)
                        i = s.in_reply_to_status_id
                        omit = 1
                    html = ''.join(embed['html'] for embed in tweets[::-1])
                    publication.twitter_thread = html
                    twitter_threads[publication.last_tweet_in_thread] = html
