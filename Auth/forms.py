from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'image', 'user',)
        widgets = {'user': forms.HiddenInput()}


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        # self.fields['password'].widget.attrs['hidden'] = 'hidden'


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter email address'}))
    first_name = forms.CharField(max_length=100, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=100, label='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter username'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<small class="form-text text-muted">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<small class="form-text text-muted"><ul class="list-unstyled"><li class="list-item">Your password cannot be too similar to your other personal information.</li><li class="list-item">Your password must contain at least 8 characters.</li><li class="list-item">Your password cannot be a commonly used password.</li><li class="list-item">Your password cannot be entirely numeric.</li></ul></small>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<small class="form-text text-muted">Enter the same password as before, for verification.</small>'
