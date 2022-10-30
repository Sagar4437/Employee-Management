from django.shortcuts import redirect, render

from employee_register.forms import EmployeeForm
from employee_register.models import Employee

# Create your views here.
def employee_list(request):
    employee_list = Employee.objects.all()
    return render(request, 'employee_register/employee_list.html',{'employee_list':employee_list})

def employee_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            '''its insert operation'''
            form = EmployeeForm()
        else:
            '''its update operation'''
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)

        return render(request, 'employee_register/employee_form.html',{'form':form})   

    if request.method == 'POST':
        if id == 0:
            '''its insert operation'''
            form = EmployeeForm(request.POST)
        else:
            '''its update operation'''
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
        return redirect(employee_list)

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect(employee_list)
