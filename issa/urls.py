from django.conf.urls import url, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
#   url(r'^api/register/$', RegisterAPI.as_view(), name='register'),
    url(r'^registerPage/$', views.signPage, name='signPage'),
    url(r'^search/$', views.search_results, name='search_results'),
    url(r'^new/activity$', views.activities, name='new-activities'),
    url(r'^user/$',views.user,name = 'new-user'),
    url(r'^new_user/$',views.new_user,name = 'new_profile'),
    url(r'^edit_profile/$',views.edit_user,name = 'edit_profile'),
    url(r'^businesses/$',views.businesses,name = 'biz'),
    url(r'^display/$',views.display_business,name = 'display_business'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
