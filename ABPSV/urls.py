"""ABPSV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from WebApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('girl/',views.gretrieve,name='girl'),
    path('gvote/<int:id>',views.gvote,name='gvote'),
    path('gshow/<int:id>',views.gshow,name='gshow'),
    path('boy/',views.bretrieve,name='boy'),
    path('bvote/<int:id>',views.bvote,name='bvote'),
    path('',views.vlogin,name='vlogin'),
    path('afterlogin/',views.afterlogin),
    path('result/',views.result,name='result'),
    path('adm/',views.admprof,name='admin'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('admboy/',views.admboy,name='admboy'),
    path('bcreate/',views.orgcreate),
    path('bretrieve/<int:id>',views.bret,name='bretrieve'),
    path('bupdate/<int:id>',views.bupdate,name='bupdate'),
    path('bdelete/<int:id>',views.bdelete,name='bdelete'),
    path('admgirl/',views.admgirl,name='admgirl'),
    path('gcreate/',views.gcreate),
    path('gretrieve/<int:id>',views.gret,name='gretrieve'),
    path('gupdate/<int:id>',views.gupdate,name='gupdate'),
    path('gdelete/<int:id>',views.gdelete,name='gdelete'),
    path('admvoter/',views.admvoter,name='admvoter'),
    path('vcreate/',views.vcreate),
    path('vretrieve/<int:id>',views.vret,name='vretrieve'),
    path('vupdate/<int:id>',views.vupdate,name='vupdate'),
    path('vdelete/<int:id>',views.vdelete,name='vdelete')


]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
