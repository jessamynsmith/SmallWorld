
from django.conf.urls import url
from meetings import views

urlpatterns = [

    url(r'^$', views.MeetingListView.as_view(), name='meetings_list'),

    url(r'^(?P<pk>[0-9]+)/user/initial/$', views.MeetingView.as_view(), name="user_meeting_initial"),

    url(r'^(?P<meetingpk>[0-9]+)/student/create/$', views.StudentMeetingCreateView.as_view(), name="student_meeting_create"),

    url(r'^student/update/(?P<pk>[0-9]+)/$', views.StudentMeetingUpdateView.as_view(), name="student_meeting_update"),

    url(r'^(?P<meetingpk>[0-9]+)/mentor/create/$', views.MentorMeetingCreateView.as_view(), name="mentor_meeting_create"),

    url(r'^mentor/update/(?P<pk>[0-9]+)/$', views.MentorMeetingUpdateView.as_view(), name="mentor_meeting_update"),




    # /TeamMap/team_id/
    # url(r'^meetings/(?P<meetingpk>[0-9]+)/student/?P<studentpk>[0-9]+)$', views.StudentMeetingUpdateView.as_view(), name='student_meeting_update'),  # detailview expects id







]