from django.http import Http404
from rest_framework import status
from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import PublicScreenshot
from .serializers import PublicScreenshotSerializer
from scrshot_api.permissions import IsOwnerOrReadOnly


class PublicScreenshotList(generics.ListCreateAPIView):
    serializer_class = PublicScreenshotSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    queryset = PublicScreenshot.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PublicScreenshotDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PublicScreenshotSerializer
    queryset = PublicScreenshot.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
