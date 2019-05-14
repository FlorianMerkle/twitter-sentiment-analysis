from tweepy import Cursor, TweepError
import tweepy
from twitter.twitter_client import get_twitter_client

def get_tweets(q, mode):
    client=get_twitter_client()
    tweets = []
    try:
        # own timeline
        #res = Cursor(client.home_timeline, tweet_mode='extended', lang='en').items(2)
        # or
        # search for string
        if mode == 'hashtag_search':
            res = Cursor(client.search, q=q, tweet_mode='extended', lang = 'en').items(100)
            comment_type = 'Twitter Hashtag'
        elif mode == 'replies':
            res = Cursor(client.search, q=q, tweet_mode='extended', lang = 'en').items(100)
            comment_type = 'Twitter Reply'
        for status in res:
            '''if 'retweeted_status' in status._json:
                #print('retweet')
                #print(status.retweeted_status)
                #print(status.retweeted_status.created_at)
                #print(status._json)
                
                    
                tweet = {
                    'type': comment_type,
                    'status_id': status.retweeted_status.id,
                    'author': status.retweeted_status.user.screen_name,
                    'created_at': status.retweeted_status.created_at.isoformat(),
                    'text': status.retweeted_status.full_text,
                    'shares': status.retweeted_status.retweet_count,
                    'likes': status.retweeted_status.favorite_count,
                    'author_follower_count': status.retweeted_status.user.followers_count,
                    'link':'https://twitter.com/' + status.retweeted_status.user.screen_name + '/status/' + str(status.retweeted_status.id)
                }
                
                if 'lang' in status.retweeted_status._json:
                    tweet.update({'language': status.retweeted_status.lang})
                if 'place' in status.retweeted_status._json and status.retweeted_status._json['place'] is not None:
                    tweet.update({'country': status.retweeted_status.place.country})
                else:
                    tweet.update({'country': 'N/A'})
                tweets.append(tweet)
                #print(tweet)'''
            if 0==1:
                print ('0 is 1')
            else:
                #print('no retweet')
                #print(status)
                tweet={
                    'type': comment_type,
                    'status_id': status.id,
                    'author': status.user.screen_name,
                    'created_at': status.created_at.isoformat(),
                    'text': status.full_text ,
                    'shares': status.retweet_count,
                    'likes': status.favorite_count,
                    'author_follower_count': status.user.followers_count,
                    'link':'https://twitter.com/' + status.user.screen_name + '/status/' + str(status.id)}
                if 'lang' in status._json:
                    tweet.update({'language': status.lang})
                if 'place' in status._json and status._json['place'] is not None:
                    tweet.update({'country': status.place.country})
                else:
                    tweet.update({'country': 'N/A'})
                tweets.append(tweet)
        return tweets
    except TweepError as e:
        print('could not get tweets',e.reason)
        return(e.reason)