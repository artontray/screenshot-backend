from rest_framework import serializers
from category.models import Category
from .models import PrivateScreenshot
from scrshot_api.permissions import IsOwner


class PrivateScreenshotSerializer(serializers.ModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    category_id = serializers.ReadOnlyField(source='owner.category.id')
    category_title = serializers.ReadOnlyField(source='owner.category.title')
    #category = serializers.PrimaryKeyRelatedField(
    #    many=True, queryset=Category.objects.all().filter(owner__username='admin'))

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


    def get_fields(self, *args, **kwargs):
        '''
        Function to only shows category owned by logged current user
        '''
        fields = super(PrivateScreenshotSerializer, self).get_fields(*args, **kwargs)
        request = self.context['request']
        owner = request.user
        fields['category'].queryset = fields['category'].queryset.filter(owner=owner)
        return fields


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        permission_classes = [IsOwner]
        model = PrivateScreenshot
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
            'category_id',
            'category',
            'category_title',
        ]