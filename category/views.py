from django.http import Http404
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from scrshot_api.permissions import IsOwnerOrReadOnly, IsOwner, IsLoggedIn


class CategoryList(APIView):
    """
    List all Category for the logged user
    No Create view (post method), as profile creation handled by django signals
    """
    permission_classes = [IsLoggedIn]
    serializer_class = CategorySerializer
    def get(self, request):
        categories = Category.objects.all().filter(owner=request.user)
        self.check_object_permissions(self.request, categories)
        serializer = CategorySerializer(
            categories, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

class CategoryDetail(APIView):
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