from django import forms
from django.core.validators import validate_email, validate_slug

def verifySuggestion(value):
    if len(value)<10:
        raise forms.ValidationError("Not Long Enough")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return value

def verifySuggestion2(value):
    if value[0]=='H':
        raise forms.ValidationError("Can't start w/ H")
    # Always return the cleaned data, whether you have changed it or
    # not.
    return value

class Suggestion_Form(forms.Form):
    suggestion = forms.CharField(validators=[verifySuggestion2,verifySuggestion,validate_slug],label='Suggestion', max_length=240)
