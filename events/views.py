from rest_framework import generics, permissions, filters
from pp5_drf_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Event
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    """
    Retrieve events from DB.
    Create new events.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()

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


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update & Destroy events.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()