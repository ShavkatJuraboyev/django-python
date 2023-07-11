from django.shortcuts import render
from .models import Jobs, Employees, Dependents, Departments, Locations, Regions, Countries


# from django.db.models import Q, Count, Min, Max, Avg

def index_page(request):
    return render(request, 'index.html')


def max_salary(request, id):
    queryset = Employees.objects.all().order_by('-salary')[:id]
    return render(request, 'salary.html', {"max_salary": queryset})


def get_dependent(request, employee_id):
    queryset = Dependents.objects.all().filter(employee=employee_id)
    employee = Employees.objects.get(employee_id=employee_id)
    context = {
        'deps': queryset,
        'employee': employee,
    }
    return render(request, 'dependent.html', context)


def get_job(request, id):
    queryset = Jobs.objects.all().order_by("min_salary")[:id]
    return render(request, 'jobs.html', {'job': queryset})


def get_employee(request, job_id):
    queryset = Employees.objects.all().filter(job_id=job_id)
    return render(request, 'employe.html', {'epm': queryset})


def get_departments(request):
    queryset = Departments.objects.all()
    context = {"depar": queryset}
    return render(request, 'departments.html', context)


def get_location(request, location_id):
    queryset = Locations.objects.all().filter(location_id=location_id)
    context = {'loc': queryset}
    return render(request, 'location.html', context)


def get_region(request):
    queryset = Regions.objects.all()
    return render(request, 'region.html', {'reg': queryset})


def get_country(request, region_id):
    queryset = Countries.objects.all().filter(region_id=region_id)
    return render(request, 'country.html', {'coun': queryset})


def get_coun_location(request, country_id):
    queryset = Locations.objects.all().filter(country_id=country_id)
    context = {'cloc': queryset}
    return render(request, 'coun_location.html', context)

# def orm_site(request):
#     # queryset = Employees.objects.filter(Q(first_name__startswith='K'), Q(last_name__startswith='C'))
#     # queryset = Employees.objects.filter(salary__range=(2500, 9000))
#     # queryset = Employees.objects.filter(~ Q(employee_id=110))
#     # queryset = Countries.objects.filter(region__region_id=1)
#
#     # distinct = Employees.objects.values('first_name').annotate(name_count=Count('first_name')).filter(name_count=2)
#     # records = Employees.objects.filter(first_name__in=[item['first_name'] for item in distinct])
#     # queryset1 = Employees.objects.filter(employee_id__gte=100)
#     # queryset2 = Employees.objects.filter(employee_id__lte=117)
#     # queryset1 = union(queryset2)
#     # queryset = Employees.objects.all().aggregate(Avg('job_id'))
#     # queryset = Employees.objects.values('job_id').annotate(soni=Count('job_id'))
#     # queryset = Employees.objects.select_related('job').first()
#     queryset = Jobs.objects.prefetch_related('employees_set').get(job_id=9)
#     qs = list(queryset.employees_set.all())
#     http = ''
#     for i in qs:
#         http += F"<li>{i.first_name}</li>"
#         print(i.first_name)
#     return HttpResponse(f"<ol>{http}</ol>")
