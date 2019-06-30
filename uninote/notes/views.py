from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q
from django.http import *
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound


def homepage(request):

    
    deptset=Departments.objects.all()
    return render(request=request,template_name='notes/home.html',context={'deptset':deptset})


def getnotes(request):


    department=request.GET['dept']


    department=request.GET['dept']

    for x in Departments.objects.all():
        
        dept_info={}
        if x.dept==department:
            

            dept_info['dept']=x.dept
            dept_info['HOD']=x.HOD

            break



    form=GetNotes(initial={'department':department},auto_id=True)
    return render(request=request,template_name='notes/getnotes.html',context={'form':form,'dept_info':dept_info})




def displaynotes(request):

    dept=request.GET['department'].replace('+','%20')
    sub=request.GET['subject']
    yr=request.GET['year']

    queryset=Notes.objects.all()
    queryset=queryset.filter(Q(department__dept=dept),Q(subject__subject=sub),Q(year=yr))

    l=[]

    for x in queryset:
        
        d={}
        d['department']=x.department.dept
        d['year']=x.year
        d['subject']=x.subject.subject
        
        file_list=[]

        for f in x.files.all():

            file_list.append((f.files.url,f.image.url))

        d['files']=file_list
         
        l.append(d)

        return render(request=request,template_name='notes/displaypdf.html',context={'mydata':l})

def pdf_view(request):

    pass
    
    



    

    
