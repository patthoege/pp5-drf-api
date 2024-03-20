from rest_framework import serializers
from .models import Event
from saved.models import Save


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for Events model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    save_id = serializers.SerializerMethodField()
    saved_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Return to correct user.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_save_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            save = Save.objects.filter(
                owner=user, event=obj
            ).first()
            return save.id if save else None
        return None

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'title', 'content', 'date', 'time',
            'place', 'event_link', 'category', 'created_on',
            'modified_on', 'is_owner', 'profile_id', 'profile_image',
            'save_id', 'saved_count', 'comments_count'
        ]
