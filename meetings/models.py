
from django.db import models
from users.models import Student, Mentor

class Meeting(models.Model):
    name = models.CharField(max_length=100)
    video = models.CharField(max_length=50)
    info = models.CharField(max_length=1000)

    def __str__(self):
        return "{}".format(self.name)

class StudentMeeting(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    web_task = models.CharField(max_length=1000)

    def __str__(self):
        return "{} {}".format(self.student, self.meeting)


class MentorMeeting(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    team_data = models.CharField(max_length=1000)

    def __str__(self):
        return "{} {}".format(self.mentor, self.meeting)






