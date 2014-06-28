from django.conf.urls import patterns, url

urlpatterns = patterns('webcalc.views',
	url(r'^projects/$', 'project_list'),
	url(r'^projects/(?P<pk>[0-9]+)/$', 'project_detail')


	)