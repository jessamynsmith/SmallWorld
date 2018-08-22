# users/views.py

from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView
from users.models import CustomUser, Student, Mentor
from django.contrib import messages
from django.contrib.auth import login

from .forms import StudentSignUpForm, MentorSignUpForm


class ChooseRoleView(TemplateView):
    template_name = 'users/role.html'

    def home(request):
        if request.user.is_authenticated:
            if request.user.is_student:
                return redirect('TeamMap:team-add')
            else:
                return redirect('users:role')
        return render(request, 'home/home.html')


class StudentSignUpView(CreateView):
    model = CustomUser
    form_class = StudentSignUpForm
    template_name = 'users/signup.html'
    # success_url = reverse_lazy('login')

    # success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        user = super(StudentSignUpView, self).get_context_data(**kwargs)
        # user = super(UserCreationForm, self).save(commit=False)
        return user

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class MentorSignUpView(CreateView):
    model = CustomUser
    form_class = MentorSignUpForm
    template_name = 'users/signup.html'
    # success_url = reverse_lazy('login')

    # success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'mentor'
        user = super(MentorSignUpView, self).get_context_data(**kwargs)
        return user
        # return super().get_context_data(**kwargs)
        # user = super(UserCreationForm, self).save(commit=False)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginView(TemplateView):
    template_name = 'users/registration/login.html'


# class GenericSignUp(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'
#
# class Home(TemplateView):
#     template_name = 'home.html'

# class StudentSignUp(GenericSignUp):
#     is_student = True
#     is_mentor = False
#
# class MentorSignUp(GenericSignUp):
#     is_student = False
#     is_mentor = True

# class UserFormView(View):
#     form_class = UserForm#hwat is form class, blueprint for form
#     template_name = 'TeamMap/registration_form.html' #html file that form going to be included in
#
#     #display blank form, don't have account yet
#     def get(self,request):
#         form = self.form_class(None) #use UserForm, pass no data yet
#         return render(request, self.template_name, {'form': form})
#
#     #process form data, add to db
#     def post(self,request):
#         form = self.form_class(request.POST)#request.POST = what they input, when submit becomes post data, pass to form, form validates it
#
#         if form.is_valid():
#             user = form.save(commit = False) #user object using whatever they typed in the form, creates obj from for, does not save to db yet, stores it locally
#
#             #cleaned (normalized) data = data formatted properly
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             #when change user passoword take user object. Calls et passowrd
#             user.set_password(password)
#             user.save()
#
#             #returns USer objects if credentials are correct
#             user = authenticate(username=username, password=password) #takes u and p, and check sdb to see if exist
#
#             if user is not None:
#                 if user.is_active: #account not disabled
#                     login(request, user) #pass in request and user, that's it, now logged in
#                     #can refer to them as request.user.username
#                     return redirect('TeamMap:index') #redirect after log in
#
#
#         return render(request, self.template_name, {'form': form}) #if unsuccessfu, try again

#

