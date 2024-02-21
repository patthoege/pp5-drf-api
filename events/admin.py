from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'content',
        'date',
        'time',
        'place',
        'event_link',
        'category', 
        'created_on'
    )
    search_fields = ['title', 'content', 'category']
    list_filter = ('created_on', 'modified_on')