from rest_framework import serializers
from .models import Category
from private_screenshots.models import PrivateScreenshot


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    private_screenshots_count = serializers.SerializerMethodField()

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

    def get_private_screenshots_count(self, obj):

        return PrivateScreenshot.objects.all().filter(
            category__id=obj.id).count()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Category
        ordering = ['-private_screenshots_count']
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'title',
            'description',
            'image',
            'is_owner',
            'profile_id',
            'profile_image',
            'private_screenshots_count',
        ]
