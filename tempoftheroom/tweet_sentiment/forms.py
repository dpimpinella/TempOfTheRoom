from django import forms
from django.shortcuts import render
from requests import request


class QueryForm(forms.Form):
    query = forms.CharField(label='Enter search query', max_length=200)


        

