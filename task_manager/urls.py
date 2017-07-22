from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^login/$', auth_views.login, {'template_name': 'tasks/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,  name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('tasks.urls')),
]