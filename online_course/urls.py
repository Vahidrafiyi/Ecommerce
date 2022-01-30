from django.urls import path
from django.conf.urls import url, include
from online_course.views import OnlineCourseView, ChapterViewSet, EpisodeViewSet ,OnlineCourseViewSet
from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('chapter', ChapterViewSet, basename='chapter')
router.register('episode', EpisodeViewSet)
router.register('online_course', OnlineCourseViewSet)
urlpatterns = [
    #path('', OnlineCourseView.as_view()),
    url('',include(router.urls)),
    # path('episode', EpisodeViewSet.as_view()),
]












# from django.urls import path
# from django.conf.urls import url, include
# from online_course.views import OnlineCourseViewSet, ChapterViewSet, EpisodeViewSet
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
#
# router.register('', OnlineCourseViewSet)
# router.register('episode', EpisodeViewSet)
# router.register('chapter', ChapterViewSet)
#
# urlpatterns = [
#     url('',include(router.urls)),
# ]