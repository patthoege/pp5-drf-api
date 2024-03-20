from django.db import models
from django.contrib.auth.models import User
from events.models import Event


class Save(models.Model):
    """
    Save model, related to 'owner' and 'events'.
    'owner' is a User instance and 'events' is a Event instance.
    'unique_together' makes sure a user can't save the same event twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, related_name='saved', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'event']

    def __str__(self):
        return f'{self.owner} {self.event}'
