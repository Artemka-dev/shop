import django_filters

from .models import Product
from django.db.models import Max, Min

from django.forms.widgets import TextInput

class FilterProducts(django_filters.FilterSet):

    VIDEOS = (
        ("4K Format", "4K Format"),
        ("Full", "Full HD (1080p)"),
        ("HD 720", "HD (720p)"),
        ("SD 480", "SD (480p)")
    )

    TYPES = (
        ("цена", "Скидка 20%"),
        ("хит", "Хит сезона")
    )

    videoformat = django_filters.ChoiceFilter(label="Разрешение видео", choices=VIDEOS, method='get_videoformat')
    typeof = django_filters.ChoiceFilter(label="Тип товара", choices=TYPES, method="get_types")

    min_price = django_filters.CharFilter(label="От", method="get_min_price", widget=TextInput(attrs={"placeholder": "Минимальная цена"}))
    max_price = django_filters.CharFilter(label="До", method="get_max_price", widget=TextInput(attrs={"placeholder": "Максимальная цена"}))

    title_product = django_filters.CharFilter(label="Название товара", method="get_title", widget=TextInput(attrs={"placeholder": "Название товара"}))

    def get_videoformat(self, queryset, name, value):
        return queryset.filter(desc__icontains=value)

    def get_types(self, queryset, name, value):
        return queryset.filter(status=value)


    def get_min_price(self, queryset, name, value):
        max_price = Product.objects.all().aggregate(Max("price"))['price__max']
        return queryset.filter(price__range=(value, max_price))

    def get_max_price(self, queryset, name, value):
        min_price = Product.objects.all().aggregate(Min("price"))['price__min']
        return queryset.filter(price__range=(min_price, value))

    def get_title(self, queryset, name, value):
        return queryset.filter(title__icontains=value)