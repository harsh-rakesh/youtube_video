from django.urls import path
from . import views

urlpatterns = [
    path('videos/', views.PaginatedVideoView.as_view(), name='paginated_videos'),
    path('search/', views.SearchVideoView.as_view(), name='search_videos'),
    path('fetch/', views.FetchVideosView.as_view(), name='fetch_videos'),
]