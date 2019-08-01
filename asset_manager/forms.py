from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from asset_manager.models import User, Employee


class EmployeeSignUpForm(UserCreationForm):
    name = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super.save(commit=False)
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(user=user)
        employee.name.add(*self.cleaned_data.get('name'))
        return user


class EmployerSignUpForm(UserCreationForm):
    pass