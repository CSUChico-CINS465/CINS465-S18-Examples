from django.urls import path, include
# import django.contrib.auth.urls
# import django
from . import views
from .forms import LoginForm
from django.contrib.auth import views as adminviews

urlpatterns = [
    path('',views.index),
    path('suggestion/',views.suggestion_view),
    path('suggestions/',views.suggestion_api),
    path('page<int:page_num>/',views.page),
    path('login/', adminviews.login, {
        'template_name':'registration/login.html',
        'authentication_form':LoginForm
    }, name="login"),
    path('logout/', adminviews.logout,{
        'next_page':'/login/'
    }),
    path('register/', views.register),
    #path('accounts/', include('django.contrib.auth.urls')),
]
