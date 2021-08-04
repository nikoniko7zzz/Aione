from django.shortcuts import render
from django import forms

class NewForm(forms.Form):
    keyword1 = forms.CharField(label='keyword1', max_length=100)
    keyword2 = forms.CharField(label='keyword2', max_length=100)