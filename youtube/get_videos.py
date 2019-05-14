from youtube.youtube_client import get_youtube_client

'''
This function takes a Youtube channel id 
It returns a list with the id's of all videos uploaded by this channel
'''

def get_channel_videos(YOUTUBE_CHANNEL_ID):
    client = get_youtube_client()
    upload_playlist_id = get_upload_playlist_id(client, YOUTUBE_CHANNEL_ID)
    res = client.playlistItems().list(part = 'snippet', playlistId = upload_playlist_id, maxResults = 50).execute()
    video_ids = []
    for item in res['items']:
        video_ids.append(item['snippet']['resourceId']['videoId'])
    return video_ids
    

def get_upload_playlist_id(client, YOUTUBE_CHANNEL_ID):
    res = client.channels().list(part = 'contentDetails', id = YOUTUBE_CHANNEL_ID).execute()
    #print(YOUTUBE_CHANNEL_NAME)
    return res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    