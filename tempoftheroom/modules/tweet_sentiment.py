import requests
import json
import base64
import urllib

class OAuthToken:
    """Contains API key information used for authentication when sending 
    Twitter API requests.
    """
    API_OAUTH_ENDPOINT = 'https://api.twitter.com/oauth2/token'
    API_CONSUMER_KEY = ''
    API_SECRET_KEY = ''

    def __init__(self):
        self.bearer_token = self.request_bearer_token()

    def request_bearer_token(self):
        key_secret = '{}:{}'.format(
            OAuthToken.API_CONSUMER_KEY,
            OAuthToken.API_SECRET_KEY)
        b64_encoded_key = base64.b64encode(key_secret.encode('ascii'))
        b64_encoded_key = b64_encoded_key.decode('ascii')

        headers = {
            'User-Agent':'TemperatureOfTheRoom',
            'Authorization':'Basic ' + b64_encoded_key,
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
            'Accept-Encoding':'gzip'} 
        body = {'grant_type':'client_credentials'}
        request = requests.post(
            OAuthToken.API_OAUTH_ENDPOINT,
            data = body,
            headers = headers)

        bearer_token = request.json()['access_token']
        return bearer_token

class TwitterSearch:
    """UTF-8 and URL encodes query to Twitter Search API and stores the 
    resulting text from the Tweets in a list.
    """
    API_SEARCH_ENDPOINT = 'https://api.twitter.com/1.1/search/tweets.json?q='

    def __init__(self, query, token):
        self.query = self.modify_query(query)
        self.token = token
        self.count = 2
        self.lang = 'en'
        self.tweet_mode = 'extended'
        self.Url_suffix = self.build_suffix()
        self.search_results = self.send_search(token)
        self.tweet_text = self.find_text()        

    def modify_query(self,query):
        modified_query = "{} -filter:retweets -filter:replies".format(query)
        return modified_query

    def send_search(self,token):
        encoded_query = urllib.parse.quote(self.query.encode('utf-8'))
        url = self.API_SEARCH_ENDPOINT + encoded_query + self.Url_suffix
        headers = {
            'User-Agent':'TemperatureOfTheRoom',
            'Authorization':'Bearer ' + self.token,
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
        response = requests.get(url, headers = headers)
        results = json.loads(response.content)
        return results

    def build_suffix(self):
        suffix = '&count={}&lang={}&tweet_mode={}'.format(self.count, self.lang, self.tweet_mode)
        return suffix
    
    def find_text(self):
        tweet_text = []
        for item in self.search_results['statuses']:
            tweet_text.append(item['full_text'])
        return tweet_text

class SentimentAnalysis:
    """Sends Tweet text to http://text-processing.com/api/sentiment/ and stores
    the response.
    """
    SENTIMENT_API_ENDPOINT = 'http://text-processing.com/api/sentiment/'

    def __init__(self, tweet_text):
        self.tweet_text = tweet_text
        self.sentiment_results = self.total_results()

    def get_sentiment(self, text):

        headers = {
            'X-Mashape-Key':'Zx3Hnd9BrvmshEBx4i5UfCZlJqHKp1ddegSjsnmdXY62V9Ndsh',
			'Content-Type':'application/x-www-form-urlencoded',
			'Accept':'application/json'}
        body = {'language':'english', "text":text}
        response = requests.post(
            SentimentAnalysis.SENTIMENT_API_ENDPOINT,
            data = body,
            headers = headers)
        sentiment_result = json.loads(response.content)
        sentiment_result = sentiment_result['label']
        if (sentiment_result == 'pos'):
            sentiment_result = 'Positive'
        if (sentiment_result == 'neg'):
            sentiment_result = 'Negative'
        if (sentiment_result == 'neutral'):
            sentiment_result = 'Neutral'
        return sentiment_result
    
    def total_results(self):
        sentiment_results = []
        for item in self.tweet_text:
            sentiment_results.append(self.get_sentiment(item))
        return sentiment_results






