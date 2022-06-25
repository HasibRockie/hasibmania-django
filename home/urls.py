from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/',views.allposts, name="posts"),
    path('personals/',views.personals, name="personals"),
    path('religious/',views.religious, name="religious"),
    path('fictions/',views.fictions, name="fictions"),
    path('gratitude/',views.gratitude, name="gratitude"),
    path('post/<str:id>/',views.post, name="post"),
]

