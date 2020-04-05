from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse

from items.models import Product
from django.views.generic import View, TemplateView, FormView, DetailView, DeleteView, ListView, UpdateView

from .forms import ProductForm
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

# Is Super Usera
class SuperuserRequiredMixin(object):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(SuperuserRequiredMixin, self).dispatch(*args, **kwargs)


class AdminMain(SuperuserRequiredMixin, TemplateView):
	template_name = "admin_panel/admin_main.html"

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['active'] = "admin_main"
		context['products'] = Product.objects.all()
		return context
		

class EditProduct(SuperuserRequiredMixin, UpdateView):
	model = Product
	form_class = ProductForm
	template_name = 'admin_panel/edit.html'
	pk_url_kwarg = "id"
	success_url = reverse_lazy("admin_page")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['element'] = Product.objects.get(id=self.kwargs['id'])
		return context

class CreateProduct(SuperuserRequiredMixin, FormView):
	form_class = ProductForm
	success_url = "admin_page"
	template_name = 'admin_panel/create.html'

	def form_valid(self, form):
		form.save()
		return redirect(self.get_success_url())


class DeleteProduct(SuperuserRequiredMixin, DeleteView):
	model = Product
	success_url = reverse_lazy("admin_page")
	pk_url_kwarg = "id"
	template_name = "admin_panel/product_confirm_delete.html"


class ReadProduct(SuperuserRequiredMixin, DetailView):
	model = Product
	pk_url_kwarg = "id"
	template_name = "admin_panel/product_detail.html"


class CheckUsers(SuperuserRequiredMixin, ListView):
	template_name = "admin_panel/check_users.html"
	model = User
	context_object_name = "users"

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['active'] = "users"
		return context