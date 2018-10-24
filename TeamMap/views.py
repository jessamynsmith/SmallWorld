
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from TeamMap.models import Team, TeamStudent
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from users.models import Mentor
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#can create custom mixin in mixins.py
#inherit from mixin you care about, use it everywhere you want it

class IndexView(generic.ListView): #inherit from ListView
    template_name = 'TeamMap/index.html' #what template we are using to display albums- when get list of albums, plug into this template
    context_object_name = 'allTeams' #makes object_list = allTeams

    def get_queryset(self): #queryset function- query database for teams we want
        return Team.objects.all()

class DetailView(generic.DetailView): #data about 1 object
    model = Team #what model trying to get details for
    template_name = 'TeamMap/detail.html' #when you get the team, what template do you want me to plug into

class TeamCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView): #SWnote - this function will be used by mentors to create team
    model = Team
    fields = ['name', 'location', 'level', 'team_logo','accepting_members', 'bigIssue' ]#what field do you need user to fill out
    success_url = reverse_lazy('TeamMap:index')  #thought 'TeamMap' was https
    #reverse is used to get actual url from url name. called immediately when python file is parsed, when server starts up.
    #don't want to call reverse until django is up and running b/c it would fail
    #_lazy means won't be run until actually needs to be, until trying to redirect
    #reverse is mapping from names to urls

    def test_func(self):
        return self.request.user.is_mentor
    #     self.request= in a class based view, always have access to self.request. if you put login required, there is logged in user
    #     self.request.user is whoever is logged in- always

    def form_valid(self, form):
        # gets called when form validation passed
        #based on model, dj will generate form. for required fields, required on form
        self.object = form.save(commit=False)
        mentor = self.request.user.mentor
        self.object.mentor = mentor
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        # setting variables that you can access in the template
        # context = context template will be rendered in
        #a lot of default contexts- which is why you make the super call
        context = super(TeamCreate, self).get_context_data(**kwargs)
        #super is calling parent's get context data
        #actually calling parent of TeamCreate, actually passing CreateView
        # print (context)
        context['mentor'] = self.request.user.mentor
        return context

class TeamUpdate(UpdateView):  # SWnote - this function will be used by mentors to create team
    model = Team
    fields = ['name', 'location', 'numMembers', 'level', 'team_logo' ]  # what field do you need user to fill out

class TeamDelete(DeleteView):
    model = Team #after delete, where want to go?
    success_url = reverse_lazy('TeamMap:index')

class TeamStudentCreateView(generic.CreateView):
    model = TeamStudent
    fields = []  #have to put fields in, even if blank
    success_url = reverse_lazy('TeamMap:index')

    def _get_team(self):
        teampk = self.kwargs.get('teampk')
        team = Team.objects.filter(pk=teampk).first()
        return team
    # need helper function for level of code (not a necessity)
    # because get team involves 1)value from self.kwargs then 2)db look up on that
    # turn code into function -1) limit repetition 2) easier to understand
    # could have a get student

    def form_valid(self, form):
        self.object = form.save(commit=False)
        team = self._get_team()
        self.object.team = team
        student = self.request.user.student
        self.object.student = student
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(TeamStudentCreateView, self).get_context_data(**kwargs)
        context['team'] = self._get_team()
        return context

    #shift tab- tabs left



































