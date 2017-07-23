from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from tasks.views import CreateUser

urlpatterns = [
	url(r'^login/$', auth_views.login, {'template_name': 'tasks/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'tasks/logout.html'}, name='logout'),
    url(r'^new-user/$', CreateUser.as_view(), name='create_user'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('tasks.urls')),
]