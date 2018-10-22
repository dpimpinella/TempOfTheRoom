from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from modules.tweet_sentiment import OAuthToken
from modules.tweet_sentiment import TwitterSearch

from .forms import QueryForm

# Create your views here.

class Index(FormView):
    
    template_name = 'tweet_sentiment/index.html'
    form_class = QueryForm
    success_url = "results"

    def form_valid(self, form):
        ### TODO you are able to get quesy from form, now how do you use it.
        data = form.cleaned_data
        data = data["query"]
        return super().form_valid(form)

class Results(TemplateView):
    template_name = 'tweet_sentiment/results.html'
    





