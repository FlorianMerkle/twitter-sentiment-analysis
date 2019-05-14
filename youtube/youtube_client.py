import config
from apiclient.discovery import build

def get_youtube_client():
    client = build('youtube', 'v3', developerKey = config.YOUTUBE_API_KEY)
    return (client)
