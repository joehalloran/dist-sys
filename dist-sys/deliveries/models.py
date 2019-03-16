from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
	nickname = models.CharField(max_length=200)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.nickname
    
class Address(models.Model):
	line_one = models.CharField(max_length=200)
	line_two = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	postcode = models.CharField(max_length=10)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

	def __str__(self):
		return self.line_one

class Product(models.Model):
	product_name = models.CharField(max_length=200)
	brand_name = models.CharField(max_length=200)
	list_price = models.IntegerField(default=0)
	
	def __str__(self):
		return self.product_name

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	order_date = models.DateTimeField('order date')
	shipping_date = models.DateTimeField('shipping date')
	shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product)
		




	