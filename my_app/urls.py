from django.urls import path
from .views import my_site, first_site, fanlar


urlpatterns = [
    path('', my_site, name="my_site"),
    path('tatusf/', first_site, name="first_site"),
    path('tatusf/ax/', fanlar, name="fanlar"),

]