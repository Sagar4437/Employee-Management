from django import forms
from django import forms

from employee_register.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels ={
            'fullname':'Full Name',
            'emp_code': 'Employee ID',
        }

    def __init__(self,*args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_lable = "Select"
        # self.fields['emp_code'].required = False
