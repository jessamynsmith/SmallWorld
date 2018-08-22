
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

# from TeamMap.models import (myUser, Student)


# class StudentSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#
#     def save(self, commit=True):
#         user = super.save(commit=False)
#         user.is_student = True
#         if commit:
#             user.save()
#         return user