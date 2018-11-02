from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from modules.tweet_sentiment import OAuthToken
from modules.tweet_sentiment import TwitterSearch
from modules.tweet_sentiment import SentimentAnalysis
from modules.tweet_sentiment import Oembed
from .forms import QueryForm

import urllib

class Index(FormView):
    """Defines home page."""
    
    template_name = 'tweet_sentiment/index.html'
    form_class = QueryForm
    success_url = 'results'

    def form_valid(self, form):
        return super().form_valid(form)


class Results(TemplateView):
    """Defines results page."""
    template_name = 'tweet_sentiment/results.html'
    
    def send_twitter_search(self, query):
        """Creates bearer token via OAuthToken and sends search to Twitter Search 
        API for a given query.

        Args:
            query: The text to be sent to Twitter Search API.
        
        Returns:
            search: A TwitterSearch object for a given query.
        """
        token = OAuthToken().bearer_token
        search = TwitterSearch(query, token)
        return search
    
    def get_oembed_html(self, search):
        """Gets the HTML that will be used in conjunction with Twitter's 
        Javascript loader to embed tweets.

        Args: 
            search: A TwitterSearch object containing the URLs of the Tweets 
            that will be embedded.

        Returns:
            html: A list containing the HTML for each Tweet.
        """
        encoded_urls = []
        for url in search.urls:
            url = urllib.parse.quote_plus(url.encode('utf-8'))
            encoded_urls.append(url)

        oembed = Oembed(encoded_urls)
        html = oembed.get_html()
        return html


    def post(self, request):
        """Creates the dictionary to be used with results.html to display 
        search/sentiment results for a given search in the browser.

        Returns:
            A dictionary containing the a string representing the user's query 
            and a 'results' list containing the sentiment results for each 
            Tweet, as well as the HTML that will be used to embed those Tweets.
        """
        query = request.POST.get('query')  
        search = self.send_twitter_search(query)
        html = self.get_oembed_html(search)
        tweet_text_list = search.tweet_text
        results_list = SentimentAnalysis(tweet_text_list).sentiment_results
        results = list(zip(results_list, html))
        context = {'query':query, 'results':results}
        return render(request, 'tweet_sentiment/results.html',  context)


    





