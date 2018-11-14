# API Project

This application connects two APIs: The Twitter Standard Search API and the Text-Processing Sentiment Analysis API.
The goal was to analyze the sentiment of Tweets for a given search criteria, in order to gauge their "temperature" (i.e., are the Tweets positive or negative).

The flow of this application is:

User enters search query -> query is sent to Search API -> the Tweet text is pulled from the response -> Tweet text is sent to Sentiment Analysis API -> sentiment for each Tweet is displayed

## Part 1: Tweet Sentiment module

This module contains Python code that gets authentication in order to send requests to Twitter, sends the requests, and processes the responses. It also handles sending requests to and processing responses from the Sentiment Analysis API.

Twitter's Search API is extensive, so this could be modified to conduct searches with different criteria, or it could be changed to interact with one of the many other APIs Twitter offers.

## Part 2: Displaying the results in a browser with Django

The second part of the project was to create a way for the user to interface with the Tweet Sentiment module. This was done with Django, so that the user interaction could take place within a web browser.  The application allows the user to submit a query, and then displays the results of the sentiment analysis with the corresponding text from each Tweet.

<p align="center">
  <img width="640" height="400" src="https://github.com/dpimpinella/Python2/blob/master/API%20Project/images/walkthrough_v2.gif">
</p>
