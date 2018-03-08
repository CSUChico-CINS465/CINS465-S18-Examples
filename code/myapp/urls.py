from django.urls import path

from . import views

urlpatterns = [
    path('',views.index),
    path('suggestion/',views.suggestion_view),
    path('suggestions/',views.suggestion_api),
    path('page<int:page_num>/',views.page),
]
