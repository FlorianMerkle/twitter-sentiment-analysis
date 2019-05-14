from youtube.youtube_client import get_youtube_client
from youtube.get_videos import get_channel_videos

def get_comments(YOUTUBE_CHANNEL_ID):
        video_ids = get_channel_videos(YOUTUBE_CHANNEL_ID)
        client = get_youtube_client()
        comments = []
        for video_id in video_ids:
                res = client.commentThreads().list(part = 'snippet, replies' ,videoId=video_id, maxResults = 2).execute()
                for item in res['items']:
                        replies = get_replies(item, client)
                        comments.extend(replies)
                        top_level_comment = get_top_level_comment(item, client)
                        comments.extend(top_level_comment)
        print(50 * '^')
        print (len(comments))
        return comments

def get_top_level_comment(item,client):
        comments = []
        top_level_comment = item['snippet']['topLevelComment']
        author_details = get_author_details(top_level_comment['snippet']['authorChannelId']['value'], client)
        comment = {
                'type':'Youtube Comment',
                'comment_id': top_level_comment['id'], 
                'author': top_level_comment['snippet']['authorDisplayName'], 
                'created_at': top_level_comment['snippet']['publishedAt'], 
                'text': top_level_comment['snippet']['textOriginal'], 
                'video_id': top_level_comment['snippet']['videoId'], 
                'likes': top_level_comment['snippet']['likeCount'], 
                'author_follower_count':  author_details['subscriber_count'], 
                'country': author_details['country'], 
                'shares': 'N/A',
                'link': 'https://www.youtube.com/watch?v=' + top_level_comment['snippet']['videoId'] + '&lc=' + top_level_comment['id']
                }
        comments.append(comment)
        return comments

def get_replies(item, client):
        comments = []
        if 'replies' in item:
                for reply in item['replies']['comments']:
                        author_details = get_author_details(reply['snippet']['authorChannelId']['value'], client)
                        comment = {
                                'type':'Youtube Comment',
                                'comment_id': reply['id'], 
                                'author': reply['snippet']['authorDisplayName'],
                                'created_at': reply['snippet']['publishedAt'],
                                'text': reply['snippet']['textOriginal'],
                                'video_id': reply['snippet']['videoId'],
                                'likes': reply['snippet']['likeCount'],
                                'author_follower_count': author_details['subscriber_count'],
                                'country': author_details['country'],
                                'shares': 'N/A',
                                'link': 'https://www.youtube.com/watch?v=' + reply['snippet']['videoId'] + '&lc=' + reply['id']
                                }
                        comments.append(comment)
        return comments

def get_author_details(id, client):
        res = client.channels().list(part='snippet,statistics', id = id).execute()
        if 'country' in res['items'][0]['snippet']:
                country = res['items'][0]['snippet']['country']
        else:
                country = 'N/A'
        return {'subscriber_count': res['items'][0]['statistics']['subscriberCount'], 'country': country}
    