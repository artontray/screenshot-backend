from django.http import Http404
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PrivateScreenshot
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters
from .serializers import PrivateScreenshotSerializer
from scrshot_api.permissions import IsOwner

class PrivateScreenshotList(generics.ListCreateAPIView):
    serializer_class = PrivateScreenshotSerializer
    permission_classes = [IsOwner]

    

    # queryset = PrivateScreenshot.objects.all().filter(owner=user).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'category',
    ]
    search_fields = [
        'content',
        'title',
    ]
    def get_queryset(self):
        return PrivateScreenshot.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
  

class PrivateScreenshotDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    serializer_class = PrivateScreenshotSerializer

    def get_queryset(self):
        return PrivateScreenshot.objects.all().filter(owner=self.request.user)









        

