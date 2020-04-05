from django.db import models


from django.contrib.auth.models import User
import django.utils.timezone as d


# Create your models here.
class Product(models.Model):
	
	title = models.CharField("Название товара", max_length=150, db_index=True)
	desc = models.TextField("Описание товара", blank=True, db_index=True)
	price = models.IntegerField("Цена товара", db_index=True)
	status = models.TextField("Статус товара", db_index=True, default="хит")
	category = models.IntegerField("Категория товара", db_index=True, blank=True)
	picture = models.ImageField("Изображение", upload_to="pictures/", null=True, blank=True, default='default/default.jpg')


	comments = models.ManyToManyField('CommentProduct', blank=True, related_name="products")

	date_public = models.DateField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.title

	def set_price(self):
		self.price = int(str(self.price).replace(" ", ''))

		return int(self.price - (20 * self.price / 100))

	# category_product.html
	def get_description(self):
		self.desc = self.desc.split(";")[:3]

		return self.desc

	def get_max_videoformat(self):
		max_videoformat = self.desc.split(";")[0].split(":")[1]

		return str(max_videoformat)

	def get_full_desc(self):
		return self.desc.split(";")

	class Meta:
		verbose_name = "Продукт"
		verbose_name_plural = "Продукты"

class CommentProduct(models.Model):
	user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

	adv = models.TextField("Достоинства", blank=True, db_index=True)
	dis_adv = models.TextField("Недостатки", blank=True, db_index=True)
	comment = models.TextField("Коментарий", blank=True, db_index=True)

	date_pub = models.DateField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return self.comment

class Basket(models.Model):
	user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
	id_product = models.IntegerField(blank=True, null=True, db_index=True, unique=True)

	def __str__(self):
		return str(self.id_product)