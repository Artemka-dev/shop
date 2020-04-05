from django.urls import path
from .views import *

urlpatterns = [
	path('admin_main_page/', AdminMain.as_view(), name="admin_page"),
	path('edit_product_<id>/', EditProduct.as_view(), name="edit_page"),
	path('create_product/', CreateProduct.as_view(), name="create_page"),
	path('delete_product_<int:id>/', DeleteProduct.as_view(), name="delete_page"),
	path("read_product_<int:id>/", ReadProduct.as_view(), name="read_page"),
	path("check_users/", CheckUsers.as_view(), name="check_users")
]