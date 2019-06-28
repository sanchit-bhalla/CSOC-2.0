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


    form=GetNotes(initial={'department':department},auto_id=True)
    return render(request=request,template_name='notes/getnotes.html',context={'form':form})




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

        #fs = FileSystemStorage()
        
        for f in x.files.all():

            file_list.append(f.files.name)

##            filename = f.files.name
##            if fs.exists(filename):
##                 with fs.open(filename) as pdf:
##                    response = HttpResponse(pdf, content_type='application/pdf')
##                    response['Content-Disposition'] = 'inline; filename=f.files.name'
##                    return response
##            else:
##                    return HttpResponseNotFound('The requested pdf was not found in our server.')


        
        d['files']=file_list
        
        l.append(d)

    return JsonResponse(l,safe=False)

def pdf_view(request):

    pass
    
    



    

    
