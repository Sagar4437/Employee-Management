from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.employee_form, name='employee_insert'), #type:ignore
    path('update/<int:id>', views.employee_form, name='employee_update'), #type:ignore
    path('list/', views.employee_list,name='employee_list'),
    path('delete/<int:id>', views.employee_delete, name='employee_delete'), #type:ignore

 
]