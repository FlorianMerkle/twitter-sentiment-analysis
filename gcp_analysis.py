import config
from google.cloud import language

def analyze_post(tweet):
    path = config.GOOGLE_CREDENTIALS
    client = language.LanguageServiceClient.from_service_account_json(path)
    document = language.types.Document(
        content = tweet,
        type = 'HTML'
    )
    try:
        sentiment_analysis = get_sentiment_analysis(client, document)
    except Exception as e:
        print(e)
    try:
        category = get_categories(client, document)
    except Exception as e:
        print(e)
    return sentiment_analysis['score'], sentiment_analysis['magnitude'], category


def get_sentiment_analysis(client, document):
    try:
        res = client.analyze_sentiment(document = document)
        score = res.document_sentiment.score
        magnitude = res.document_sentiment.magnitude
        #print(score)
        #return score, magnitude
    except Exception as e:
        print('Error at get_sentiment analysis: ', e)
        # set sentiment to zero 
        score = 0
        magnitude = 0
        #return (e)
    return {'score':score,'magnitude': magnitude}

def get_categories(client, document):
    try:
        res = client.classify_text(document = document)
        #print (res)
        return(res.categories[0].name[1:])
    except Exception as e:
        print('Error at get_categories: ', e)
        return ('N/A')