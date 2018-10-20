from django.conf.urls import url
from tweet_sentiment import views

urlpatterns = [ 
    url(r'^$', views.HomePageView.as_view()),
]