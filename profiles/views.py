from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework import generics, filters
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django_filters.rest_framework import DjangoFilterBackend
from scrshot_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    List all profiles
    No Create view here, profile creation handled by django signals
    """
    queryset = Profile.objects.annotate(
        public_screenshots_count=Count('owner__publicscreenshot', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
    ]
    search_fields = [
        'owner__username',
    ]
    ordering_fields = [
        'public_screenshots_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
        
    ]

class ProfileDetail(generics.RetrieveUpdateAPIView):
    '''
    Edit or update (not delete) Profil only if owner
    '''
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        public_screenshots_count=Count('owner__publicscreenshot', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')