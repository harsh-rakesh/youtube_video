# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /youtube_video

# Install Python dependencies
COPY requirements.txt /youtube_video/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . /youtube_video/

# Run migrations and collect static files
RUN python manage.py migrate

# Command to run the application
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "youtube_video.asgi:application", "--bind", "0.0.0.0:8000"]
# CMD ["bash", "-c", "celery -A youtube_video worker --loglevel=info & gunicorn -k uvicorn.workers.UvicornWorker youtube_video.asgi:application --bind 0.0.0.0:8000"]