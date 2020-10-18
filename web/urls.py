
from django.contrib import admin
from django.urls import path
from ecourse.views import *
urlpatterns = [
    path('admin/', admin.site.urls ),
    path('',start),
    path('login',login),
    path('signup',signup),
    path('courses',courses),
    path('courses/<cname>',getvid),
    path('courses/<cname>/vid/<vno>',playvid),  
]
