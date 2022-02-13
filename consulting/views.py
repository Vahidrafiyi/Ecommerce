from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from consulting.models import ConsultationForm
from consulting.serializers import ConsultSerializer

class ConslutFormAPI(APIView):
    def get(self):
        query = ConsultationForm.objects.all()
        serializer = ConsultSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ConsultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)