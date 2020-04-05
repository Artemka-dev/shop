from django import forms
from .models import CommentProduct

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

class CommentForm(forms.ModelForm):

	class Meta:
		model = CommentProduct
		fields = ['adv', 'dis_adv', 'comment']
		

class ChangeForm(UserChangeForm):

	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name']

		labels = {
			'username': _('Имя пользователя'),
			'email': _("Ваша почта"),
			'first_name': _("Ваше имя"),
			'last_name': _('Ваша фамилия')
		}