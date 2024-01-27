from celery.app import shared_task
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.discovery import build

# Set up the YouTube API client

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def search_videos(api_key, search_query, max_results=5):
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_google.json"

    youtube = build(api_service_name, api_version, developerKey=api_key)

    request = youtube.search().list(
            part="snippet",
            type="video",
            order="date",
            q=search_query,
            maxResults=max_results
        )

    response = request.execute()

    videos = []
    for item in response.get("items", []):
        video = {
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
            "publish_time": item["snippet"]["publishTime"],
            "thumbnails": item["snippet"]["thumbnails"]
        }
        videos.append(video)

    return videos