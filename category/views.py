from django.http import Http404
from rest_framework import status
from rest_framework import permissions, filters
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from .serializers import CategorySerializer
from private_screenshots.models import PrivateScreenshot
from scrshot_api.permissions import IsOwnerOrReadOnly, IsOwner, IsLoggedIn


class CategoryList(generics.ListCreateAPIView):
    """
    List all Category for the logged user
    First category creation handled by django signals when creating an New User,
    more category can be created by user.
    """
    permission_classes = [IsLoggedIn]
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
  

    def get_queryset(self):
        return Category.objects.all().filter(owner=self.request.user)

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    search_fields = [
        'title',
        'description',
    ]
    ordering_fields = [
        'private_screenshots_count',
    ]


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsOwner]
    
    def get_object(self, pk):
        try:
            categories = Category.objects.get(pk=pk)
            self.check_object_permissions(self.request, categories)
            return categories
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        categories = self.get_object(pk)
        serializer = CategorySerializer(
            categories, context={'request': request}
        )
        
        return Response(serializer.data)

    def put(self, request, pk):
        categories = self.get_object(pk)
        serializer = CategorySerializer(
            categories, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        categories = self.get_object(pk)
        # We have to check at least one category left.
        nb_categories = Category.objects.filter(owner=request.user).count()
        if nb_categories > 1:
            categories.delete()
        else:
            # Not permitted, only one category left
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(
            status=status.HTTP_204_NO_CONTENT
    )