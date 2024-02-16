from rest_framework import generics, permissions
from pp5_drf_api.permissions import IsOwnerOrReadOnly
from followers.models import Follower
from followers.serializers import FollowerSerializer


# Class provided by DRF-API walkthrough.
class FollowerList(generics.ListCreateAPIView):
    """
    List followers or create a follow if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Class provided by DRF-API walkthrough.
class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follow or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()