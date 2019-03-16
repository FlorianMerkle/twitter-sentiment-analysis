from tweepy import OAuthHandler
from tweepy import API
import config

def get_twitter_auth():
    try:
        consumer_key = config.TWITTER_CONSUMER_KEY
        consumer_secret = config.TWITTER_CUSTOMER_SECRET
        access_token = config.TWITTER_ACCESS_TOKEN
        access_secret = config.TWITTER_ACCESS_SECRET
    except KeyError:
        print("Could not authenticate to Twitter")
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return(client)