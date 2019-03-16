from gcp_get_sentiment import get_google_cloud_sentiment_scores
from twitter_collector import get_tweets, get_timeline
import pandas

if __name__ == '__main__':
    #data = get_tweets()
    data = get_timeline()
    #print (data)
    tweets = []
    sentiment = []
    magnitude = []
    for index, tweet in enumerate(data):
        res = get_google_cloud_sentiment_scores(tweet)
        tweets.append(tweet)
        sentiment.append(round(res[0], 2))
        magnitude.append(round(res[1], 2))
    gc = list(zip(tweets, sentiment, magnitude))
    columns = ['Tweet', 'Sentiment', 'Magnitude']
    gc_df = pandas.DataFrame(gc, columns = columns)
    path = '/Users/florianmerkle/dev/twitter/tables/tables.csv'
    gc_df.to_csv(index = True, path_or_buf = path)