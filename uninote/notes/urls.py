from django.urls import path
from . import views
from django.conf import settings

app_name='notes'



urlpatterns=[
               path('',views.homepage,name='homepage'),
               path('getnotes',views.getnotes,name='getnotes'),
               path('displaynotes',views.displaynotes,name='displaynotes'),
               path('pdfview',views.pdf_view,name='pdfview'),

    ]

