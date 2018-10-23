from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.edit import View
from modules.tweet_sentiment import OAuthToken
from modules.tweet_sentiment import TwitterSearch
from modules.tweet_sentiment import SentimentAnalysis
from .forms import QueryForm

# Create your views here.

class Index(FormView):
    
    template_name = 'tweet_sentiment/index.html'
    form_class = QueryForm
    success_url = 'results'

    def form_valid(self, form):
        return super().form_valid(form)


class Results(TemplateView):
    template_name = 'tweet_sentiment/results.html'

    def send_twitter_search(self, query):
        token = OAuthToken().bearer_token
        search = TwitterSearch(query, token)
        return search.tweet_text

    def post(self, request):
        query = request.POST.get('query')  
        tweet_text_list = self.send_twitter_search(query)
        results_list = SentimentAnalysis(tweet_text_list).sentiment_results
        results = list(zip(tweet_text_list,results_list))
        print(results)
        context = {'query':query, 'results':results}
        return render(request, 'tweet_sentiment/results.html',  context)
    


    





