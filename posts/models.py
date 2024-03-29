from django.db import models
from django.contrib.auth.models import User


# Class provided by DRF-API walkthrough.
class Post(models.Model):
    """
    Posts Model related to Owner/User.
    """
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    location = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='images/', default='../default_post_oug5vu', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        """
        Order posts by date created.
        Display by most recent first.
        """
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
