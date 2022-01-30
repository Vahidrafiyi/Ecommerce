from django.urls import path
from django.conf.urls import include,url
from certification.views import *

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('certificate',CertificateView,basename='certificate')

urlpatterns=[
    url('',include(router.urls)),
    path('certificatee/<int:pk>/',CertificateApi.as_view()),
    path('certificate_edit/<int:pk>/',CertificateEditApi.as_view()),
    path('certificate_search/',CertificateSearch.as_view()),
    path('certificate_search_all/',CertificateSearchAll.as_view()),
    path('certificate_filter_search/',CertificateFilterSearch.as_view()),
    # path('search/',UserListView.as_view()),
    path('ssearch/',CertificateList.as_view()),


]

