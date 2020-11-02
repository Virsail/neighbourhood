from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^registerPage/$', views.signPage, name='signPage'),
    url(r'^search/$', views.search_results, name='search_results'),
    #url(r'^project/(\d+)', views.get_project, name='project_results'),
    #url(r'^new/project$', views.new_project, name='new-project'),
    #url(r'^accounts/profile/$', views.user_profiles, name='profile'),
    
    #url(r'api/project/project-id/(?P<pk>[0-9]+)/$',
    #    views.ProjectDescription.as_view())
  
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
