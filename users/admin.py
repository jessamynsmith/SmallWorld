# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import StudentSignUpForm, MentorSignUpForm, CustomUserChangeForm
from .models import CustomUser, Student, Mentor

class CustomUserAdmin(UserAdmin):
    add_form = StudentSignUpForm, MentorSignUpForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'is_mentor', 'is_student']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Mentor)