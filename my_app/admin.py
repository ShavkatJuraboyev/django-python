from django.contrib import admin
from .models import University, Fakultet, Kafedralar, Fanyonalishlar, Yonalishlar
# Register your models here.


admin.site.register(University)
admin.site.register(Fakultet)
admin.site.register(Kafedralar)
admin.site.register(Fanyonalishlar)
admin.site.register(Yonalishlar)