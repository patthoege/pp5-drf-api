from rest_framework import generics, permissions
from pp5_drf_api.permissions import IsOwnerOrReadOnly
from saved.models import Save
from saved.serializers import SaveSerializer


class SaveList(generics.ListCreateAPIView):
    """
    Saved list or create a save if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
