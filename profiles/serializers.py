from rest_framework import serializers
from .models import Profile
from followers.models import Follower
from public_screenshots.models import PublicScreenshot
from private_screenshots.models import PrivateScreenshot


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    nb_screenshots_public = serializers.SerializerMethodField()
    nb_screenshots_private = serializers.SerializerMethodField()

    def get_nb_screenshots_public(self, obj):
        return PublicScreenshot.objects.all().filter(owner=obj.owner).count()

    def get_nb_screenshots_private(self, obj):
        return PrivateScreenshot.objects.all().filter(owner=obj.owner).count()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            # print(following)
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'description',
            'image',
            'is_owner',
            'following_id',
            'posts_count',
            'followers_count',
            'following_count',
            'nb_screenshots_public',
            'nb_screenshots_private',
        ]
