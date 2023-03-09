from rest_framework import serializers
from .models import PublicScreenshot
from likes.models import Like

class PublicScreenshotSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'height too big, max is 4096px'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'width too big, max is 4096px!'
            )
        return value


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, public_screenshot=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = PublicScreenshot
        fields = [
            'id',
            'owner', 
            'created_at', 
            'updated_at', 
            'title', 
            'content', 
            'image', 
            'is_owner',
            'profile_id',
            'profile_image',
            'like_id', 
            'likes_count', 
            'comments_count',
        ]