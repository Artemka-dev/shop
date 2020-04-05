from django import forms

from items.models import Product
from django.utils.translation import gettext_lazy as _

# Create your forms
class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ['title', 'desc', 'price', 'status', 'category', 'picture']

		CHOICES = (("хит", "хит"), ("цена", "цена"))
		CATEGORIES = (("1", "камеры"), ("2", "экшн-камеры"))

		widgets = {
			'title': forms.TextInput(attrs={"autocomplete": "off"}),
			'desc': forms.Textarea(attrs={"autocomplete": "off"}),
			'price': forms.TextInput(attrs={"autocomplete": "off"}),
			'status': forms.Select(choices=CHOICES),
			'category': forms.Select(choices=CATEGORIES)
		}
