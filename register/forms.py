from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from register.models import Singers


class Voter(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(Voter, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control', 'placeholder': 'Confirm Password'})
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Login ID', 'class': 'form-control'})
        self.fields['email'].widget = forms.TextInput(attrs={'placeholder': 'example@example.com', 'class': 'form-control'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Singer(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    bio = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'I\'m a rockstar, baby!', 'class': 'form-control'}))
    img = forms.FileField(help_text='Insert Image')

    class Meta:
        model = Singers
        fields = '__all__'


class Login(forms.Form):
    username = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Login ID', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
