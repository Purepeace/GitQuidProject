from django.conf.urls import url
from GitQuid import views


app_name = 'GitQuid'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),

    # url(r'^add_category/$', views.add_category, name='add_category'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
    #                views.show_category, name='show_category'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/add_project/', views.add_project, name='add_project'),

    # Account related urls
    url(r'^register/$', views.register, name='register'),
    url(r'^account/(?P<slug>[-\w]+)/$', views.account, name='account'),
    url(r'^account/(?P<slug>[-\w]+)/editProfile/$', views.editProfile, name='editProfile'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),

    # Project related urls
    url(r'^projects/$', views.browseProjects, name='browseProjects'),
    url(r'^projects/addProject/$', views.addProject, name='addProject'),
    url(r'^projects/(?P<slug>[-\w]+)/editProject$', views.editProject, name='editProject'),
    url(r'^projects/(?P<slug>[-\w]+)/viewProject$', views.viewProject, name='viewProject'),
]
