from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from event_log.models import LogUserActivity
from event_log.serializers import LogUserSerializer
class LogUserAPI(APIView):
    def get(self, request):
        query = LogUserActivity.objects.all()
        serializer = LogUserSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
