from django.urls import path
from .views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', Main.as_view(), name="main_page"),
	path('product_<int:id>/', ProductPage.as_view(), name="product_detail_page"),
	path('profile/', Profile.as_view(), name="profile_page"),
	path('edit_comment_<int:id>/', EditComment.as_view(), name="edit_comment"),
	path('delete_comment_<str:id>/', delete_comment, name="delete_comment_page"),
	path('category/<int:cat>/', RenderCategory.as_view(), name='category_page'),
	path('add_to_basket_<int:id>/', add_to_basket, name='add_to_basket'),
	path('basket/', BasketProducts.as_view(), name="basket_products_page"),
	path('delete_<int:id>/', delete_from_basket, name='delete_from_basket'),
	path("page_query/", search_query, name="search_page"),
	path("password/", password, name="password_red")
]