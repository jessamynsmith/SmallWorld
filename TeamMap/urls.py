from django.conf.urls import url
from . import views #dot means same directory

# from TeamMap.views import students, mentors



urlpatterns = [
    # /TeamMap/ is the pattern, index references this pattern
    url(r'^$', views.IndexView.as_view(), name= 'index'), #how to set up index for each individual page

    # /TeamMap/team_id/ is the pattern- detail references this pattern
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name= 'detail' ), #detailview expects id

    # /TeamMap/team/add/ - don't need to make pk, after create it will be assigned pk
    url(r'team/add/$', views.TeamCreate.as_view(), name='team-add'),

    # /TeamMap/team/2/
    url(r'team/(?P<pk>[0-9]+)/$', views.TeamUpdate.as_view(), name='team-update'),

    # /TeamMap/team/2/delete - don't need to make pk, after create it will be assigned pk
    url(r'team/(?P<pk>[0-9]+)/delete/$', views.TeamDelete.as_view(), name='team-delete'),

    url(r'^team/(?P<teampk>[0-9]+)/join/$', views.TeamStudentCreateView.as_view(), name='team_student_create'),
    #teampk is same as pk, but when have foreignkey to 2 things, need to specficy (should specify)
    #updateview needsn another primary key



]



