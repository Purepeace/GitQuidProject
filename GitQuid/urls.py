from django.conf.urls import url
from GitQuid import views

# !!!
# Commented everything because:
# python manage.py sqlmigrate GitQuid 0001 can't run if some django code doesn't compile
# Pov
# !!!

app_name = 'GitQuid'
urlpatterns = [
    # url(r'^$',views.index,name='index'),
    # url(r'^about/',views.about, name='about'),
    # url(r'^add_category/$', views.add_category, name='add_category'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
    #                views.show_category, name='show_category'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/add_project/', views.add_project, name='add_project'),
    # url(r'^signup/$',views.signup,name='signup'),
    # url(r'^login/$',views.login, name='login'),
    # url(r'^restricted/',views.restricted,name='restricted'),
    # url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
]