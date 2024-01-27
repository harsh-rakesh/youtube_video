import time
from celery.app import shared_task
from video_manager.youtube import search_videos
from .models import Video
from .config import Youtube

@shared_task
def fetch_and_store_videos(search_query):
    while True:
        try:
            # Fetch latest videos
            latest_videos = search_videos(api_key=Youtube.APIKey, search_query = "")
    
            # Store videos in the database
            for video_data in latest_videos:
                Video.objects.create(
                    title=video_data["title"],
                    description=video_data["description"],
                    publishing_datetime=video_data["publish_time"],
                    thumbnails_url=video_data["thumbnails"]
                )
        except Exception as e:
            # Handle exceptions (logging, alerting, etc.)
            print(f"Error: {str(e)}")
            break

        # Wait for the next interval (10 seconds)
        time.sleep(10)