from django.urls import path
from Myapp import views

urlpatterns = [
    path('',views.Home),
    path('company',views.Company),
    path('employee',views.Employee),
    path('searchingCom',views.SearchingCom),
    path('searchingEmp',views.SearchingEmp),
    path('EmployeeData',views.EmployeeData),
    path('CompanyData',views.CompanyData),
    path('EmpData',views.EmpData),
    path('ComData',views.ComData),
    path('ViewEmpData',views.ViewEmpData),
]
