from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from meetings.models import StudentMeeting, MentorMeeting, Meeting
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.views.generic import View, TemplateView

class MeetingListView(generic.ListView): #inherit from ListView
    template_name = 'meetings/index.html' #what template we are using to display albums- when get list of albums, plug into this template
    context_object_name = 'allMeetings' #makes object_list = allTeams

    def get_queryset(self):#queryset function- query database for teams we want
        return Meeting.objects.all()
    #     meetings = Meeting.objects.none()
    #     if self.request.user.is_student or self.request.user.is_mentor:
    #         current_team = None
    #         if self.request.user.is_student:
    #             team_students = self.request.user.student.teamstudent_set.all()
    #             if team_students.count():
    #                 # Each student is only allowed one team
    #                 current_team = team_students[0].team
    #         elif self.request.user.is_mentor:
    #             current_team = self.request.user.mentor.team
    #         meetings = Meeting.objects.filter(team=current_team)
    #
    #     return meetings

        #easiest way to write it- studentmeetingcreateview and studentmeetingupdateview, on meetinginfo which link you show them depends on if they saved their info and if student:
        # updateview has id of student object
        # in template- if student, get_context_data, if meeting exists, lookup for current meeting id and current student if exist, pass to context data,
        # if meeting exists go if not create

        # return self.request.user.student.teamstudent_set.all()[0].team.meeting_set.all()
    #user has a student, student connected to team student, getting all teamstudents for this student, then arbitrarily picking first one,
    #then getting team for that teamstudent, then getting all meetings for that team


#
# class CurricView(generic.DetailView): #data about 1 object
#     model = Meeting #what model trying to get details for
#     template_name = 'meetings/detail.html' #when you get the team, what template do you want me to plug into

class MeetingView(generic.DetailView):
    model = Meeting
    template_name = 'meetings/meeting_info.html'

    def get_context_data(self, **kwargs):
        context = super(MeetingView, self).get_context_data(**kwargs)  #first, call super-- calls parent get_context_data
        if self.request.user.is_student:
            context['student_meeting'] = StudentMeeting.objects.filter(student__user=self.request.user, meeting= self.object).first()
        if self.request.user.is_mentor:
            context['mentor_meeting'] = MentorMeeting.objects.filter(mentor__user=self.request.user, meeting=self.object).first()
            #have to write query to look for student meeting obj for logged in user and this meeting
            #.objects.filter- finding a particular set of objects
            #memebr inside object not capital
            #first for performance- filter gives you whole query set back. If you do "if query set" not best- first gives you first object
            #first gives you first object
        return context






#     how to get it to recognize meetingpk

# when populating context for view, can only popualte it in view that's rendering that template




class StudentMeetingCreateView(generic.CreateView):
    model = StudentMeeting
    fields = ['web_task']
    success_url = reverse_lazy('meetings:meetings_list')

    def get_form(self, form_class=None): #don't want to override form, just customize this thing
        form = super(StudentMeetingCreateView, self).get_form(form_class)
        form.fields['web_task'].widget = forms.Textarea() #has to match name and model of form
        return form

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


class StudentMeetingUpdateView(generic.UpdateView):
    model = StudentMeeting
    fields = ['web_task']
    success_url = reverse_lazy('meetings:meetings_list')

    def get_form(self, form_class=None):  # don't want to override form, just customize this thing
        form = super(StudentMeetingUpdateView, self).get_form(form_class)
        form.fields['web_task'].widget = forms.Textarea()  # has to match name and model of form
        return form

    def get_context_data(self, **kwargs):
        context = super(StudentMeetingUpdateView, self).get_context_data(**kwargs)
        # context['meeting'] = self._get_meeting()
        print(context)
        return context




    #just get form because want to change widget

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

class MentorMeetingUpdateView(generic.UpdateView):
    model = MentorMeeting
    fields = ['team_data']
    success_url = reverse_lazy('meetings:meetings_list')

    def get_form(self, form_class=None):  # don't want to override form, just customize this thing
        form = super(MentorMeetingUpdateView, self).get_form(form_class)
        form.fields['team_data'].widget = forms.Textarea()  # has to match name and model of form
        return form

    def get_context_data(self, **kwargs):
        context = super(MentorMeetingUpdateView, self).get_context_data(**kwargs)
        # context['meeting'] = self._get_meeting()
        print (context)
        return context




