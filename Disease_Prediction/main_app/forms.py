from django import forms

class SuggestionsForm(forms.Form):
    suggestions = forms.CharField(label='Suggestions', widget=forms.Textarea)
