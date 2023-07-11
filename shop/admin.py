from django.contrib import admin
from .models import Order, Product, Category, User
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(User)