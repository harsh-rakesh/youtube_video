from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View
from .models import Video
from django.db.models import Q
from .tasks import fetch_and_store_videos

class PaginatedVideoView(View):
    def get(self, request):
        page_number = request.GET.get('page', 1)
        limit = request.GET.get('limit', 10)

        videos = Video.objects.all()
        paginator = Paginator(videos, limit)
        page = paginator.page(page_number)

        serialized_videos = [
            {
                'title': video.title,
                'description': video.description,
                'publishing_datetime': video.publishing_datetime,
                'thumbnail_urls': video.thumbnails_url,
            }
            for video in page.object_list
        ]

        return JsonResponse({'videos': serialized_videos, 'total_pages': paginator.num_pages})

class SearchVideoView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        videos = Video.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

        serialized_videos = [
            {
                'title': video.title,
                'description': video.description,
                'publishing_datetime': video.publishing_datetime,
                'thumbnail_urls': video.thumbnails_url,
            }
            for video in videos
        ]

        return JsonResponse({'videos': serialized_videos})
    

class FetchVideosView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        fetch_and_store_videos.delay(search_query=query)
        return JsonResponse({'message': 'Fetching videos in the background'})