from django.http import Http404
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PrivateScreenshot
from .serializers import PrivateScreenshotSerializer
from scrshot_api.permissions import IsOwner

class PrivateScreenshotList(APIView):
    serializer_class = PrivateScreenshotSerializer
    permission_classes = [IsOwner]

    def get(self, request):
        private_screenshots = PrivateScreenshot.objects.all()
        serializer = PrivateScreenshotSerializer(
            private_screenshots, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PrivateScreenshotSerializer(
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




class PrivateScreenshotDetail(APIView):
    permission_classes = [IsOwner]
    serializer_class = PrivateScreenshotSerializer

    def get_object(self, pk):
        try:
            private_screenshot = PrivateScreenshot.objects.get(pk=pk)
            self.check_object_permissions(self.request, private_screenshot)
            return private_screenshot
        except PrivateScreenshot.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        private_screenshot = self.get_object(pk)
        serializer = PrivateScreenshotSerializer(
            private_screenshot, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        private_screenshot = self.get_object(pk)
        serializer = PrivateScreenshotSerializer(
            private_screenshot, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        private_screenshot = self.get_object(pk)
        private_screenshot.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )










        
    def put(self, request, pk):
        PrivateScreenshot = self.get_object(pk)
        serializer = PrivateScreenshotSerializer(
            PrivateScreenshot, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
