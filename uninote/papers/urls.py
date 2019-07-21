from django.urls import path
from . import views
from .views import InvalidRequest,Warning
from django.conf import settings


app_name='papers'


urlpatterns=[
              path('',views.homepage,name='homepage'),
              path('getpapers/',views.getpapers,name='getpapers'),
              path('displaypapers/',views.displaypapers,name='displaypapers'),
              path('invalid/',InvalidRequest.as_view(extra_context={'warning1':'Please Enter Valid Request'}),name='invalid'),
              path('warning/',Warning.as_view(extra_context={'warning2':'No Files Present'}),name='warning')


    ]