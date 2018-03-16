"""GitQuidProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# !!!
# Commented everything because:
# python manage.py sqlmigrate GitQuid 0001 can't run if some django code doesn't compile
# Pov
# !!!

# fyi
# path() is like url() but it doesn't use regex for matching
# both are ok to use and does the same thing

from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from GitQuid import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^$', views.register, name='register'),
    url(r'^GitQuid/', include('GitQuid.urls')),
    # above maps any URLs starting
    # with GitQuid/ to be handled by
    # the GitQuid application
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
