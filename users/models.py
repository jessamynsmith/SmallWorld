from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    is_student = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.username)
#     takes email and explicitly makes it a string

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return "student: {}".format(self.user)


class Mentor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
        return "mentor: {}".format(self.user)

# fix this