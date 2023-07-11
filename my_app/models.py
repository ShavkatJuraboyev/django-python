from django.db import models


# Create your models here.


# Unvesiterlar
class University(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)

    def __str__(self):
        return self.name


# Raxbariyatlar
# class Leadership(models.Model):
#     first_name = models.CharField(max_length=100, blank=False, null=False)
#     last_name = models.CharField(max_length=100, blank=False, null=False)
#     email = models.EmailField(max_length=100, blank=True, null=True)
#     phone = models.IntegerField(max_length=20, blank=True, null=True)
#     position = models.CharField(max_length=100, blank=False, null=False)
#     university = models.ForeignKey(University, null=True, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.position


class Fakultet(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    university = models.ForeignKey(University, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Kafedralar(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    fakultet = models.ForeignKey(Fakultet, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Fanyonalishlar(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Yonalishlar(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    kafedralar = models.ForeignKey(Kafedralar, null=True, on_delete=models.CASCADE)
    fanlar = models.ManyToManyField(Fanyonalishlar)

    def __str__(self):
        return self.name
