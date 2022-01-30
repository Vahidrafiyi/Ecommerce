from django.template.defaulttags import url
from django.urls import path
from django.conf.urls import include,url
# from rest_framework import routers

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('menu_cat',MenuCategoryView)
router.register('menu_item',MenuItemView)
router.register('menu',MenuList)


urlpatterns = [
    url('',include(router.urls)),
    path('show_menu_category/', ShowMenuCategory.as_view()),
    path('add_menu_category/', AddMenuCategory.as_view()),
    path('show_menu_item/', ShowMenuItem.as_view()),
    path('add_menu_item/<int:pk>/', AddMenuItem.as_view()),
    #path('menu/', MenuList.as_view(),name='menu_list'),

]
