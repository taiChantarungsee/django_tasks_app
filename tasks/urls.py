from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.task_list, name='main'),
    url(r'^task/(?P<pk>\d+)/edit/$', views.task_edit, name='task_edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteTask.as_view(),
        name='task_delete',),
    url(r'^complete/(?P<pk>\d+)/$', views.task_complete, name='task_complete'),
    url(r'^add/$', views.AddTask.as_view(), name='task_add'),
]