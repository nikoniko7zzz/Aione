from django import forms

from searchs.models import Search


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('keyword1', 'keyword2', 'keyword3')