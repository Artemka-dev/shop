from django import template
from ..models import *
from django.contrib.auth.models import User
from items.models import Product

register = template.Library()

# тэг для счета количества элементов в корзине у данного пользователя
@register.simple_tag
def basket_count(username):
	return len(Basket.objects.filter(user__username=username))

# тэг для счета количества продуктов
@register.simple_tag
def products_indb():
	return len(Product.objects.all())

# тэг для счета количества пользователей
@register.simple_tag
def users_indb():
	return len(User.objects.all())

# тэг для счета количества товара в категории
@register.simple_tag
def quanity_category(category):
	return len(Product.objects.filter(category=category))