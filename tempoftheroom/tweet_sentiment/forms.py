from django import forms

class QueryForm(forms.Form):
    query = forms.CharField(label='Enter search query', max_length=200)
