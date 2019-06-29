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
from django.urls import path,include,re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.Homepage.as_view(),name='homepage'),
    re_path(r'^register_app/',include('register_app.urls',namespace='register_app')),
    re_path(r'^register_app/',include('django.contrib.auth.urls')),
    re_path(r'^about/', views.About.as_view(),name='about'),
    re_path(r'^discussions/', views.Discussions.as_view(),name='discussions'),
    re_path(r'^test/$',views.Test.as_view(),name='test'),
    re_path(r'^thanks/$',views.Thanks.as_view(),name='thanks'),
    re_path(r'^posts/',include('posts.urls',namespace='posts')),
    re_path(r'^groups/',include('groups.urls',namespace='groups')),
    path('notes/',include('notes.urls')),

    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

