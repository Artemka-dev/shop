from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product, CommentProduct, Basket
from .forms import CommentForm, ChangeForm
from .filters import FilterProducts

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

from django.views.generic import View, TemplateView, FormView, DetailView, DeleteView, ListView, UpdateView
from hashlib import md5

# artem artem123 - admin
# Artemka judo367256 - not admin

# Create your views here.
def search_query(request):
	search_input = request.GET.get("search_query", "")
	if search_input:
		search_products = Product.objects.filter(title__icontains = search_input)

	return render(request, "items/search_query.html", context={"search_products": search_products, "query": search_input})

class Main(TemplateView):
	template_name = "items/main.html"

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		products = Product.objects.all()
		context['products'] = products
		return context

class RenderCategory(TemplateView):
	template_name = 'items/category_product.html'

	def get_queryset(self):
		return Product.objects.filter(category=self.kwargs['cat'])

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['products'] = self.get_queryset()
		context['products_in_basket'] = [i.id_product for i in Basket.objects.filter(user__username=self.request.user.username)]
		context['filter'] = FilterProducts(self.request.GET, queryset=self.get_queryset())
		return context


class ProductPage(TemplateView, FormView):
	template_name = "items/product_page.html"
	form_class = CommentForm

	def form_valid(self, form):
		comment = CommentProduct.objects.create(user=self.request.user, adv=form.cleaned_data['adv'], dis_adv=form.cleaned_data['dis_adv'], comment=form.cleaned_data['comment'])
		comment.products.add(get_object_or_404(Product, id=self.kwargs['id']))
		return redirect("/")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['products_in_basket'] = [i.id_product for i in Basket.objects.filter(user__username=self.request.user.username)]
		context['product'] = get_object_or_404(Product, id=self.kwargs['id'])
		return context


class Profile(LoginRequiredMixin, View):

	def get(self, request):
		form = ChangeForm(instance=request.user)

		email = md5(request.user.email.lower().encode('utf-8')).hexdigest()
		c = CommentProduct.objects.filter(user__username=request.user.username)
		return render(request, 'items/profile.html', context={'email': email, 'form': form, 'comments': c})

	def post(self, request):
		bound_form = ChangeForm(request.POST, instance=request.user)

		if bound_form.is_valid():
			new_tag = bound_form.save()
			return redirect('profile_page')

		email = md5(request.user.email.lower().encode('utf-8')).hexdigest()
		c = CommentProduct.objects.filter(user__username=request.user.username)
		message = 'Невозможно изменить профиль'
		return render(request, 'items/profile.html', context={'email': email, 'form': bound_form, 'comments': c, 'message': message})


class EditComment(LoginRequiredMixin, UpdateView):
	model = CommentProduct
	form_class = CommentForm
	template_name = 'items/edit_comment.html'
	pk_url_kwarg = 'id'
	success_url = reverse_lazy("profile_page")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['element'] = CommentProduct.objects.get(id=self.kwargs['id'])
		return context


class BasketProducts(LoginRequiredMixin, TemplateView):
	template_name = "items/basket_products.html"

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		
		goods = []
		obj = Basket.objects.filter(user__username = self.request.user)
		for product in obj: goods.append(get_object_or_404(Product, id = product.id_product))
		context['goods'] = goods
		return context

@login_required
def delete_comment(request, id):
	element = CommentProduct.objects.get(id=id)
	element.delete()
	return redirect("profile_page")

@login_required
def delete_from_basket(request, id):
	element = get_object_or_404(Basket, id_product=id)
	element.delete()
	return redirect("basket_products_page")

@login_required
def add_to_basket(request, id):
	element = Basket.objects.create(user=request.user, id_product=id)
	return redirect("product_detail_page", id=id)

@login_required
def password(request):
	return redirect("change_password")
