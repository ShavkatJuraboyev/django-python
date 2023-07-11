from django.urls import path
from .views import index_page, max_salary, get_dependent, get_departments, get_location, get_job, get_employee, get_coun_location, get_region, get_country

urlpatterns = [
    path('', index_page, name="index"),
    path('salary/<int:id>', max_salary, name="salary"),
    path('deps/<int:employee_id>', get_dependent, name="deps"),
    path('depar/', get_departments, name="depar"),
    path('loc/<int:location_id>', get_location, name="location"),
    path('job/<int:id>', get_job, name="job"),
    path('employee/<int:job_id>', get_employee, name="employee"),
    path('region/', get_region, name='region'),
    path('country/<int:region_id>', get_country, name='country'),
    path('counloc/<str:country_id>', get_coun_location, name="counloc")
]
