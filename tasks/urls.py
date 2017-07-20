from django.conf.urls import include,url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	#url(r'^$', TemplateView.as_view(template_name='main.html')), Check why the hell this won't work
	# and while I'm at it review the old code to get the django skills back up. Then all will be ready.
    url(r'^$', views.task_list, name='main'),
    url(r'^task/(?P<pk>\d+)/edit/$', views.task_edit, name='task_edit'),
    url(r'^task/(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),
]