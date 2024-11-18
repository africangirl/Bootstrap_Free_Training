from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define a Post model to represent blog posts or articles
class Post(models.Model):
    # Title of the post with a character limit of 50
    title = models.CharField(max_length=50)
    # Main content of the post, allowing large blocks of text
    content = models.TextField()
    # Type of post (e.g., category), defaulting to 'gossip' if not specified
    Type = models.CharField(max_length=20, default='gossip')
    # Author of the post, linked to the User model; cascade deletes posts when the user is deleted
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # Timestamp for when the post was created, defaults to the current time
    created_at = models.DateTimeField(default=timezone.now)

    # Define permissions for the Post model in the Meta class
    class Meta:
        # Specifies a custom permission 'can_publish' with a descriptive name
        permissions = {
            ("can_publish", "Can publish posts"),
        }

    # String representation of the Post object, helpful for admin views and debugging
    def __str__(self):
        return f"{self.title} type:{self.Type}"  # Note: changed `self.type` to `self.Type` for consistency


# Profile model linked to the User model, providing additional user details
class Profile(models.Model):
    # One-to-one relationship with User model, which means each user has one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # A biography field that the user can leave blank
    bio = models.TextField(blank=True, null=True)
    # Location field with a character limit of 100, can also be left blank
    location = models.CharField(max_length=100, blank=True, null=True)
    # Profile picture field, allowing image uploads to the 'profile_pics/' directory
    profile_pic = models.ImageField(upload_to="profile_pics/", blank=True, null=True)

    # String representation of the Profile, showing the username for clarity
    def __str__(self):
        return f"{self.user.username}'s Profile"

# Signal receiver to automatically create or update a profile when a user is saved
@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    # If a new User instance was created, create a corresponding Profile
    if created:
        Profile.objects.create(user=instance)

