from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    Type = models.CharField(max_length=20, default='gossip')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = {
            ("can_public", "Can publish")
        }

        def __str__(self):
            return f"{self.title} type{self.Type}"

    def __str__(self):
        return self.title