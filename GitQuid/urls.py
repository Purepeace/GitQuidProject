from django.conf.urls import url
from GitQuid import views

# !!!
# Commented everything because:
# python manage.py sqlmigrate GitQuid 0001 can't run if some django code doesn't compile
# Pov
# !!!

app_name = 'GitQuid'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^about/',views.about, name='about'),
    # url(r'^add_category/$', views.add_category, name='add_category'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
    #                views.show_category, name='show_category'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/add_project/', views.add_project, name='add_project'),
    url(r'^account/$', views.account, name='account'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^projects/$', views.browse_projects, name='browse_projects'),
    url(r'^add_project/$', views.add_project, name='add_project'),
    url(r'^projectPage/$', views.projectPage, name='projectPage'),

]
