from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


# Class provided by DRF-API walkthrough.
class Comment(models.Model):
    """
    Comment model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        """
        Display comments in order of posting.
        Newest first.
        """
        ordering = ['-created_at']

    def __str__(self):
        """
        Display content instead of ID.
        """
        return self.content