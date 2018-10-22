from . import views
from django.urls import path

urlpatterns = [ 
    path('', views.Index.as_view(), name='index'),
    path('results', views.Results.as_view(), name='results'),
]