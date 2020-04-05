from django.urls import path
from .views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
	path("create_account/", CreateAccount.as_view(), name="create_account_page"),
	path("login/", LoginSite.as_view(), name="login_page"),
	path("logout/", logout, name="logout"),
	path("password/", ChangePassword.as_view(), name="change_password"),
	path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
	path('password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]