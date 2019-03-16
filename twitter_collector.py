from tweepy import Cursor
import tweepy
from twitter_client import get_twitter_client

def get_tweets():
    client=get_twitter_client()
    tweets = []
    res = Cursor(client.search, q='#horizen', tweet_mode='extended', lang = 'en').items(10)
    for status in res:
        if 'retweeted_status' in status._json:
            tweets.append(status._json['retweeted_status']['full_text'])
            #print(status._json['retweeted_status']['full_text'])
        else:
            tweets.append(status.full_text)
            #print(status.full_text)
        #print('-----------------')
    return tweets

def get_timeline():
    client=get_twitter_client()
    tweets = []
    try:
        res = Cursor(client.home_timeline, tweet_mode='extended', lang='en').items(10)
        for status in res:
            if 'retweeted_status' in status._json:
                tweets.append(status._json['retweeted_status']['full_text'])
                #print(status._json['retweeted_status']['full_text'])
            else:
                tweets.append(status.full_text)
                #print(status.full_text)
            #print('-----------------')
        return tweets
    except tweepy.TweepError as e:
        return(e.reason)