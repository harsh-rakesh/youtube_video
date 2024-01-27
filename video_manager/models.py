from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    publishing_datetime = models.DateTimeField()
    thumbnails_url = models.URLField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-publishing_datetime']
        indexes = [
            models.Index(fields=['publishing_datetime']),
            models.Index(fields=['title']),
            models.Index(fields=['description']),
        ]