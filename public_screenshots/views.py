from django.http import Http404
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PublicScreenshot
from .serializers import PublicScreenshotSerializer


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

