from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import viewsets
from rest_framework.views import APIView

from django.db.models import Q

from certification.serializers import *

from .filters import *
from rest_framework import filters

from django_filters import rest_framework as filters
from django_filters import NumberFilter,DateFilter




class CertificateView(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        certificate = Certificate.objects.all()
        return certificate

class CertificateApi(APIView):
    def get(self,request,pk):
        query=Certificate.objects.get(user_id=pk)
        print(query)
        serializers=CertificateSerializer(query)
        print(serializers.data)
        return Response(serializers.data,status=status.HTTP_200_OK)

class CertificateEditApi(APIView):
    def patch(self,request,pk):
        certificate_obj=Certificate.objects.get(user_id=pk)
        data=request.data

        certificate_obj.certificate_image_fani = data.get("certificate_image_fani", certificate_obj.certificate_image_fani)
        certificate_obj.certificate_image_academy = data.get("certificate_image_academy", certificate_obj.certificate_image_academy)
        certificate_obj.fani_score = data.get("fani_score", certificate_obj.fani_score)
        certificate_obj.academy_score = data.get("fani_score", certificate_obj.academy_score)

        certificate_obj.save()
        serializers = CertificateSerializer(certificate_obj)
        return Response(serializers.data,status=status.HTTP_201_CREATED)


class CertificateSearch(APIView):
    def get(self,request):
        search=request.GET['search']
        query=Certificate.objects.filter(course_title_fani__contains=search)
        serializers=CertificateSerializer(query,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

class CertificateSearchAll(APIView):
    def get(self,request):
        search = request.GET['search']
        query=Certificate.objects.filter(Q(course=search) | Q(online_course=search) | Q(course_title_fani=search) | Q(code_fani=search) | Q(fani_score=search) | Q(academy_score=search))
        serializers=CertificateSerializer(query,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)


class CertificateFilterSearch(APIView):
    def get(self,request):
        query=Certificate.objects.all()
        myFilter = CertificateFilter(request.GET,queryset=query)
        print(myFilter)
        serializers=CertificateSerializer(myFilter,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)


# class UserListView(generics.ListAPIView):
#     queryset = Certificate.objects.all()
#     serializer_class = CertificateSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['course_title_fani', 'user__username']

class CertificateFilter(filters.FilterSet):
    min_fani_score = NumberFilter(field_name='fani_score',lookup_expr='gte')
    max_fani_score = NumberFilter(field_name='fani_score',lookup_expr='lte')
    class Meta:
        model = Certificate
        fields = ('online_course','course')



class CertificateList(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    name = 'certificate_list'

    #filter_fields = ('course_title_fani')
    filter_class = CertificateFilter

    search_fields = ('course_title_fani','fani_score')
    ordering_fields = ('fani_score','academy_score')
