

from django.db import models
from users.models import Mentor, Student
# This gets you the user class, which you can use in admin, views, anywhere you need the user model
from django.contrib.auth import get_user_model
# You can use settings to get a reference to the class name (a string) which can be used in ForeignKey fields
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission

class Team(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length = 30)
    bigIssue = models.CharField(max_length= 30)
    level = models.IntegerField()
    team_logo = models.FileField()
    accepting_members = models.BooleanField()

    numMembers = models.IntegerField(default=0)
    #need to get rid of this as Team attribute in search field
    #summary data- alt is, every time want to know, look at number of related users
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    objects = models.Manager
    #each is column
    #each album has ID numer, goes up by 1 for each new
    #unique key = ID number

    class Meta:
        permissions = (
            ('create_team', 'Create a Team'),
            ('join_team', 'Join Team')
        )

    def get_absolute_url(self): #return details page (benchmarks) of team created
        return reverse('TeamMap:detail', kwargs={'pk': self.pk}) #pass in with pk, hidden in class Team
        #use pk of whatever team just created(viewed?)


    def __str__(self):
        return "{} {}".format(self.name, self.mentor)


class TeamStudent(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    #many to many between students and teams

    def __str__(self):
        return "{} {}".format(self.team, self.student)


class Benchmark(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    infoProj = models.CharField(max_length = 1000)
    problemState = models.CharField(max_length=200)
    is_relevant = models.BooleanField(default=False)
    DoesNotExist = models.BooleanField(default=True)
    #foreign key has id number of whatever it belongs to
    #whenever delete album, delete whatever linked to it (on_delete=models.CASCADE)

    def __str__(self):
        return "Info Project: " + self.infoProj + " Problem Statement: " + self.problemState

