import sys

from gcp_analysis import analyze_post
from twitter.twitter_collector import get_tweets
from youtube.get_comments import get_comments
from youtube.get_videos import get_channel_videos
from helpers import clean_text

import pandas


# direct link to youtube comment: https://www.youtube.com/watch?v=VIDEO_ID&lc=COMMENT_ID
# direct link to tweet: https://twitter.com/TWITTER_NAME/status/TWEET_ID

# configuration

YOUTUBE_CHANNEL_ID = 'UCrLjRdRVcuwoRv6cV7Q8A4Q' # dltlly  UCHzJ7s9HeHWrkTh8zeCnw0g #koibk UCrLjRdRVcuwoRv6cV7Q8A4Q #redbull: UCblfuW_4rakIf2h6aqANefA
TWITTER_HASHTAG = ''    #enter any seach string
TWITTER_REPLIES = ''    #enter Twitter screen name

if __name__ == '__main__':
    data = []
    if YOUTUBE_CHANNEL_ID:
        data = get_comments(YOUTUBE_CHANNEL_ID)
    if TWITTER_HASHTAG:
        data.extend(get_tweets(TWITTER_HASHTAG, 'hashtag_search'))
    if TWITTER_REPLIES:
        data.extend(get_tweets('to:' + TWITTER_REPLIES, 'replies'))
    #else:
    #    sys.exit('Provide exactly one search parameter')
    #print(data)
    comment_type, links, posts, sentiment, magnitude, date, likes, shares, author_follower_count, author_country, topic = ([] for _ in range(11))
    
    for index, tweet in enumerate(data):
        #print(tweet)
        res = analyze_post(clean_text(tweet['text']))
        comment_type.append(tweet['type'])
        shares.append(tweet['shares'])
        posts.append(tweet['text'])
        date.append(tweet['created_at'])
        likes.append(tweet['likes'])
        links.append(tweet['link'])
        author_country.append(tweet['country'])
        author_follower_count.append(tweet['author_follower_count'])
        try:
            sentiment.append(round(res[0], 2))
            magnitude.append(round(res[1], 2))
            topic.append(res[2])
            print(index)
        except Exception as e:
            print('append sentiment to list',e)
    #print(posts, sentiment, magnitude, links)
    print(comment_type, posts, topic, sentiment, magnitude, links, date, likes, author_country, author_follower_count)
    gc = list(zip(comment_type, posts, topic, sentiment, magnitude, links, date, likes, author_country, author_follower_count))
    columns = ['Type', 'Post', 'Topic', 'Sentiment', 'Magnitude', 'Links', 'Date', 'Likes', 'Author Country', 'Author Followers']
    gc_df = pandas.DataFrame(gc, columns = columns)
    path = '/Users/florianmerkle/dev/twitter/tables/tables.csv'
    gc_df.to_csv(index = True, path_or_buf = path)
    