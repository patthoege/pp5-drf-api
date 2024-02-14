from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Class provided by DRF-API walkthrough.
class Profile(models.Model):
    """
    Profile model.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(null=True, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', 
        default='../default_profile_thf96f'
    )

    class Meta:
        """
        Display profiles in order they were created.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Changing display name from ID to username.
        """
        return f"{self.owner}'s profile"
    

def create_profile(sender, instance, created, **kwargs):
    """
    Function to initiate the creation of a user profile,
    upon the creation of a new user.
    """
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)