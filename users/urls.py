

from django.conf.urls import url
from . import views

from django.views.generic import TemplateView

from views import ChooseRoleView, StudentSignUpView, MentorSignUpView
#dot means same directory

urlpatterns = [
#/TeamMap/register




    url(r'^role/$', views.ChooseRoleView.as_view(), name='role'),

    url(r'^role/student/$', views.StudentSignUpView.as_view(), name='signup-student'),

    url(r'^role/mentor/$', views.MentorSignUpView.as_view(), name='signup-mentor'),






]
#
# from django.urls import include, path
#
# from classroom.views import classroom, students, teachers
#
# urlpatterns = [
#     path('', include('classroom.urls')),
#     path('accounts/', include('django.contrib.auth.urls')),
#     path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
#     path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
#     path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
# ]