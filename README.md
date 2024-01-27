# YouTube API Project

This Django project fetches and stores YouTube videos using the YouTube API, with background tasks handled by Celery. It provides APIs to retrieve paginated video data and perform basic searches.

## Prerequisites

- Docker and Docker Compose installed on your machine.

1. Build the Docker images:
  docker-compose build
2. Start the Docker containers:
  docker-compose up

#Usage
Fetch YouTube Videos:

- To fetch YouTube videos in the background, trigger the Celery task by visiting:
  http://localhost:8000/fetch/

- API Endpoints:
Paginated Videos: http://localhost:8000/videos/
Search Videos: http://localhost:8000/search/?query=your_query

#Stop the Application:

Press Ctrl + C in the terminal where docker-compose up is running.

#Cleanup:

To stop and remove the Docker containers, run:
