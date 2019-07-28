from django.urls import path
from . import views
from .views import InvalidRequest,Warning
from django.conf import settings

app_name='notes'



urlpatterns=[

    
               path('',views.homepage,name='homepage'),
               path('getnotes',views.getnotes,name='getnotes'),
               path('displaynotes',views.displaynotes,name='displaynotes'),
               path('invalid/',InvalidRequest.as_view(extra_context={'warning1':'Wait for files to be uploaded to the server'}),name='invalid'),
               path('warning/',Warning.as_view(extra_context={'warning2':'No Files Present'}),name='warning'),

               ################################ SUPERUSER URLS #####################################
               path('choosedeptform',views.ChooseDeptForm,name='choosedeptform'),
               path('addnotesfiles',views.AddFilesForm,name='addnotesfiles'),
               path('choosedeptsem',views.ChooseDeptSem,name='choosedeptsem'),
               path('displayfiles',views.DisplayFiles,name='displayfiles'),
               path('deletefiles',views.DeleteFiles,name='deletefiles'),
               path('updatefiles/<int:id>/',views.UpdateFilesForm,name='updatefiles'),
               ############################### SUPERUSER URLS ######################################


             ]
