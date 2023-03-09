from rest_framework import generics, permissions
from scrshot_api.permissions import IsOwnerOrReadOnly, IsLoggedIn
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    List all followers, i.e. all instances of a user
    following another user'.
    """
    permission_classes = [IsLoggedIn]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower
    No Update view, as we either follow or unfollow users
    Destroy a follower, i.e. unfollow someone if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer