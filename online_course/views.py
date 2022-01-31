from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from online_course.models import OnlineCourse, Chapter, Episode
from online_course.serializers import OnlineCourseSerializer, ChapterSerializer, EpisodeSerializer
from django.http import HttpResponse
from django.contrib.auth.models import User
import datetime

class OnlineCourseViewSet(viewsets.ModelViewSet):
    queryset = OnlineCourse.objects.all()
    serializer_class = OnlineCourseSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

from django_user_agents.utils import get_user_agent

def my_view(request):
    # user_agent = get_user_agent(request)
    # if user_agent.is_mobile:
    #     print('mobile')
    # elif user_agent.is_tablet:
    #     print('tablet')
    # elif user_agent.is_pc:
    #     print('pc')
    # elif user_agent.is_bot:
    #     print('bot')
    # elif user_agent.is_touch_capable:
    #     print('touch capable')
    # print(request.user_agent.browser)  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
    # print(request.user_agent.browser.family)  # returns 'Mobile Safari'
    # print(request.user_agent.browser.version)  # returns (5, 1)
    # print(request.user_agent.browser.version_string)   # returns '5.1'
    # print(request.user_agent.)
    print(request.META['HTTP_USER_AGENT'])
    return render(request, 'alaki.html')

# def my_log():
#     if User.is_active :
#         MyLog.objects.create(user=User.username)
