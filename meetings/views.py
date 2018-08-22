from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from meetings.models import StudentMeeting, MentorMeeting, Meeting
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View, TemplateView

class MeetingListView(generic.ListView): #inherit from ListView
    template_name = 'meetings/index.html' #what template we are using to display albums- when get list of albums, plug into this template
    context_object_name = 'allMeetings' #makes object_list = allTeams

    def get_queryset(self): #queryset function- query database for teams we want
        return Meeting.objects.all()
#
# class CurricView(generic.DetailView): #data about 1 object
#     model = Meeting #what model trying to get details for
#     template_name = 'meetings/detail.html' #when you get the team, what template do you want me to plug into

class MeetingView(generic.DetailView):
    model = Meeting
    template_name = 'meetings/meeting_info.html'
#     how to get it to recognize meetingpk

class StudentMeetingCreateView(generic.CreateView):
    model = StudentMeeting
    fields = ['web_task']
    success_url = reverse_lazy('meetings:meetings_list')

    def _get_meeting(self):
        meetingpk = self.kwargs.get('meetingpk')
        meeting = Meeting.objects.filter(pk=meetingpk).first()
        return meeting

    def form_valid(self, form):
        self.object = form.save(commit=False)
        meeting = self._get_meeting()
        self.object.meeting = meeting
        student = self.request.user.student
        self.object.student = student
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(StudentMeetingCreateView, self).get_context_data(**kwargs)
        context['meeting'] = self._get_meeting()
        return context


class MentorMeetingCreateView(generic.CreateView):
    model = MentorMeeting
    fields = ['team_data']
    success_url = reverse_lazy('meetings:meetings_list')

    def _get_meeting(self):
        meetingpk = self.kwargs.get('meetingpk')
        meeting = Meeting.objects.filter(pk=meetingpk).first()
        return meeting

    def form_valid(self, form):
        self.object = form.save(commit=False)
        meeting = self._get_meeting()
        self.object.meeting = meeting
        mentor = self.request.user.mentor
        self.object.mentor = mentor
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(MentorMeetingCreateView, self).get_context_data(**kwargs)
        context['meeting'] = self._get_meeting()
        return context

