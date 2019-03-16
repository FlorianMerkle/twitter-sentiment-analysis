from google.cloud import language

def get_google_cloud_sentiment_scores(tweet):
    path = '/Users/florianmerkle/dev/twitter/ressources/twitter-sentimentalysis-b5fc18b020ca.json'
    client = language.LanguageServiceClient.from_service_account_json(path)
    document = language.types.Document(
        content = tweet,
        type = language.enums.Document.Type.PLAIN_TEXT
    )
    try:
        res = client.analyze_sentiment(document = document)
        score = res.document_sentiment.score
        magnitude = res.document_sentiment.magnitude
        return score, magnitude
    except:
        return ('google error')