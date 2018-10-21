from django.conf.urls import url
from tweet_sentiment import views
from django.urls import re_path

urlpatterns = [ 
    re_path(r'^$', views.HomePageView.as_view()),
]