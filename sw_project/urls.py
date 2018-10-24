"""sw_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
from django.urls import include, path
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static
from users import views
from home import views




urlpatterns = [


    url(r'^admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include(('home.urls', 'home'), namespace='home')),
    path('TeamMap/', include(('TeamMap.urls', 'TeamMap'), namespace='TeamMap')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('meetings/', include(('meetings.urls', 'meetings'), namespace='meetings')),
    path('about/', include(('about.urls', 'about'), namespace='about')),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),


    # url(r'^home/$', views.HomeView.as_view(), name='home'),
    # url(r'^home/$', include('Home.urls', name='home')),
    # url(r'^TeamMap/', include('TeamMap.urls', namespace = 'admin')),
    #url(r'^users/', include ('users.urls', namespace = 'users')),
    #url(r'^meetings/', include ('meetings.urls', namespace = 'meetings')),
    # url(r'^users/', include ('users.urls')),
    # url(r'^meetings/', include ('meetings.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# will check if in debug, and if yes, will attach to urlpatterns to serve up static files
urlpatterns += staticfiles_urlpatterns()
