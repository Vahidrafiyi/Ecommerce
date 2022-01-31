from django.urls import path
from django.conf.urls import url, include
from online_course.views import OnlineCourseViewSet, ChapterViewSet, EpisodeViewSet
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('online_course', OnlineCourseViewSet)
router.register('chapter', ChapterViewSet, basename='chapter')
router.register('episode', EpisodeViewSet)
urlpatterns = [
    # path('', OnlineCourseView.as_view()),
    url('',include(router.urls)),
    # path('episode', EpisodeViewSet.as_view()),
]