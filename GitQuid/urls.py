from django.conf.urls import url
from GitQuidProject import views

app_name = 'GitQuid'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^about/',views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_project/', views.add_project, name='add_project'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^login/$',views.login, name='login'),
    url(r'^restricted/',views.retricted,name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
]