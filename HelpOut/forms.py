from django import forms

class RequestForm(forms.Form):
    your_request = forms.CharField(label='', max_length=200)