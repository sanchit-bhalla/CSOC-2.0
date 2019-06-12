"""learning_users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from register_app.views import homepage,user_logout
from django.urls import include

urlpatterns = [
    re_path(r'^$', homepage,name='homepage'),
    path('admin/', admin.site.urls),
    re_path(r'^register_app/', include('register_app.urls')),
    re_path(r'^logout/', user_logout,name='logout'),

]
