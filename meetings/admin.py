from django.contrib import admin
from .models import Meeting, StudentMeeting, MentorMeeting
admin.site.register(Meeting)
admin.site.register(StudentMeeting)
admin.site.register(MentorMeeting)

