

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Student, Mentor



class StudentSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super(StudentSignUpForm, self).save(commit=False)
        user.is_student = True
        #user.set_password('new password')
        user.save()
        student = Student.objects.create(user=user)
        return user


class MentorSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super(MentorSignUpForm, self).save(commit=False)
        user.is_mentor = True
        user.save()
        mentor = Mentor.objects.create(user=user)
        return user


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'email')


