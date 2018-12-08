"""ibanapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views

import core.views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^auth/', include('social_django.urls', namespace='social')),

    re_path(r'^$', core.views.index, name='home'),
    re_path(r'^users/$', core.views.account_list, name='account_list'),
    re_path(r'^users/add/$', core.views.account_edit, name='account_add'),
    re_path(r'^users/(?P<account_id>\d{1,4})/$', core.views.account_edit, name='account_edit'),
    re_path(r'^users/(?P<account_id>\d{1,4})/delete/$', core.views.account_delete, name='account_delete'),
]
