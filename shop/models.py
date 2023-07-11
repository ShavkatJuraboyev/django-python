from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.first_name


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    payment_type = models.IntegerField()


