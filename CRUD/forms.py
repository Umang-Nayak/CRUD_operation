from django import forms
from CRUD.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["e_fname", "e_lname", "e_contact", "e_address", "e_email", "e_password"]