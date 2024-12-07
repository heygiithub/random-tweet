from django.urls import path
from .import views

urlpatterns = [
    path('',views.random_tweet, name= "random_tweet"),
]
