from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from .models import CustomUser
from .serializers import CustomUserSerializer


class UserPageAPIView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_class = permissions.IsAuthenticated

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.update_days_without_breaks()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)