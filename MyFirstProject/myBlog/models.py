from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=50)  # Changed from TextField to CharField
    content = models.TextField()
    type = models.CharField(max_length=20, default='gossip')
    created_at = models.DateTimeField(default=timezone.now)  # Automatically set the time when the object was created

    def __str__(self):
        return self.title  # Ensure this returns a string
