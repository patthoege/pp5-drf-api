from rest_framework import generics, permissions, filters
from pp5_drf_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer
from django.db.models import Count


class EventList(generics.ListCreateAPIView):
    """
    Retrieve events from DB.
    Create new events.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        saved_count =Count('saved', distinct=True)
    ).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'saved__owner__profile'
    ]

    search_fields = [
        'owner__username',
        'title',
        'place',
        'category',
    ]
    
    ordering_fields = [
        'saved_count',
        'saved__created_on',
    ]

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update & Destroy events.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        saved_count=Count('saved', distinct=True)
    ).order_by('-date')