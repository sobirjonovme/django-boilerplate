from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common import models

from . import serializers


class VersionHistoryAPIView(APIView):
    serializer_class = serializers.VersionHistorySerializer

    def get(self, request):
        query = models.VersionHistory.objects.first()
        data = self.serializer_class(query).data
        return Response(data=data, status=status.HTTP_200_OK)


__all__ = ["VersionHistoryAPIView"]
