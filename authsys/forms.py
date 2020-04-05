from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(label="Ваша почта")

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ChangeForm(UserChangeForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name']