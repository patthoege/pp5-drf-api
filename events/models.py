from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    """
    Events model.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    place = models.CharField(max_length=200)
    event_link = models.URLField('Event URL', max_length=400, blank=True)
    category = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Order events by date created.
        Display by most recent first.
        """
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title} {self.date}'
