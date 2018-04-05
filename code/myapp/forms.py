from django import forms
from django.core.validators import validate_email, validate_slug
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Suggestion_Model, Comment_Model

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
    suggestion = forms.CharField(label='Suggestion', max_length=240)
    image = forms.ImageField(label="Image File")
    image_description = forms.CharField(label='Image Description', max_length=240)

class Comment_Form(forms.Form):
    comment = forms.CharField(
        label='Comment',
        max_length=240)

    def save(self, sugg_id, req_user, commit=True):
        sugg = Suggestion_Model.objects.get(pk=sugg_id)
        comm = Comment_Model(
                comment=self.cleaned_data["comment"],
                suggestion=sugg,
                author=req_user
            )
        if commit:
            comm.save()
        return comm

class LoginForm(AuthenticationForm):
    username=forms.CharField(
        label="Username",
        max_length=30,
        widget=forms.TextInput(attrs={
            'name':'username'
        })
    )
    password=forms.CharField(
        label="Password",
        max_length=32,
        widget=forms.PasswordInput()
    )

class registration_form(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "email",
            "password1", "password2")

    def save(self, commit=True):
        user=super(registration_form,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        return user
