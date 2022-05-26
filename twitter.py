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
                publication.twitter_thread = generate_single_twitter_thread(publication.last_tweet_in_thread, twitter_threads)


def generate_single_twitter_thread(last_tweet_in_thread, twitter_threads=None):
    if twitter_threads is None:
        with shelve.open('twitter_threads_cache') as twitter_threads:
            return generate_single_twitter_thread(last_tweet_in_thread, twitter_threads=twitter_threads)
    else:
        if last_tweet_in_thread in twitter_threads:
            return twitter_threads[last_tweet_in_thread]
        else:
            get_twitter_api()
            i = last_tweet_in_thread
            tweets = []
            omit = 0
            while i is not None:
                s = twitter_api.get_status(i)
                embed = twitter_api.get_oembed('https://twitter.com/twitter/statuses/'+s.id_str, hide_thread=1, omit_script=omit, dnt=1, maxwidth=400)
                tweets.append(embed)
                i = s.in_reply_to_status_id
                omit = 1
            html = ''.join(embed['html'] for embed in tweets[::-1])
            twitter_threads[last_tweet_in_thread] = html
            return html
