from django.conf.urls import url
from FirstApp import views



urlpatterns=[
    url(r'^department$', views.departmentApi),
    url(r'^department/([0-9]+)$',views.departmentApi)

    url(r'^employees$', views.employeesApi),
    url(r'^employees/([0-9]+)$',views.employeesApi)
]