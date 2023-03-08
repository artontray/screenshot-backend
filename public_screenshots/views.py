from django.http import Http404
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PublicScreenshot
from .serializers import PublicScreenshotSerializer
from scrshot_api.permissions import IsOwnerOrReadOnly

class PublicScreenshotList(APIView):
    serializer_class = PublicScreenshotSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        PublicScreenshots = PublicScreenshot.objects.all()
        serializer = PublicScreenshotSerializer(
            PublicScreenshots, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PublicScreenshotSerializer(
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




class PublicScreenshotDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PublicScreenshotSerializer

    def get_object(self, pk):
        try:
            public_screenshot = PublicScreenshot.objects.get(pk=pk)
            self.check_object_permissions(self.request, public_screenshot)
            return public_screenshot
        except PublicScreenshot.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        public_screenshot = self.get_object(pk)
        serializer = PublicScreenshotSerializer(
            public_screenshot, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        public_screenshot = self.get_object(pk)
        serializer = PublicScreenshotSerializer(
            public_screenshot, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        public_screenshot = self.get_object(pk)
        public_screenshot.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )










        
    def put(self, request, pk):
        PublicScreenshot = self.get_object(pk)
        serializer = PublicScreenshotSerializer(
            PublicScreenshot, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
