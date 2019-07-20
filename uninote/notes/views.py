from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q
from django.http import *
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.views.generic.base import TemplateView

from django.template.defaulttags import register

@register.filter
def get_range(value):

    return range()


deptset=Departments.objects.all()


def homepage(request):

    global deptset

    
    deptset=Departments.objects.all()

    
    form=GetNotes(auto_id=True)
    return render(request=request,template_name='notes/home.html',context={'deptset_range':list(zip(deptset,list(range(len(deptset))))),'form':form})
    #return render(request=request,template_name='notes/home.html',context={'deptset':deptset,'form':form})


def department(request):

    department=request.GET['dept']

    flag=0

    for x in Departments.objects.all():

        if x.dept==department:

            flag=1

            break

    if flag==0:

            d={}
            d['dept']=department
            return JsonResponse(d)

    else:

        return HttpResponseRedirect('/invalid')

    

    
def getnotes(request):

    global deptset


    department=request.GET['dept']

    flag=0

    for x in Departments.objects.all():

        if x.dept==department:

            flag=1

            dept_info={}
            dept_info['dept']=x.dept
            dept_info['HOD']=x.HOD

            break

    if flag==0:

            return HttpResponseRedirect('invalid/')
    
    form=GetNotes(initial={'department':department},auto_id=True)
    return render(request=request,template_name='notes/getnotes.html',context={'form':form,'dept_info':dept_info,'deptset':deptset})




def displaynotes(request):

    global deptset

    dept=request.GET['department'].replace('+','%20')
    sub=request.GET['subject']
    yr=request.GET['year']

    queryset=Notes.objects.all()
    queryset=queryset.filter(Q(department__dept=dept),Q(subject__subject=sub),Q(year=yr))
    if len(queryset)==0:

        return HttpResponseRedirect('invalid/')

    else:
                             
       subject_notes=queryset[0]

       d={}
       d['department']=subject_notes.department.dept
       d['year']=subject_notes.year
       d['subject']=subject_notes.subject.subject

       file_list=[]

       for f in subject_notes.files.all():

           if f.files.name is '':
               
               return HttpResponseRedirect('warning/')
                

           else:

              file_list.append((f.files.url,f.image.url))

       d['files']=file_list


       return render(request=request,template_name='notes/displaypdf.html',context={'mydata':d,'deptset':deptset})




class InvalidRequest(TemplateView):

    template_name='notes/warning_page.html'

    def get_context_data(self,**kwargs):

        context=super().get_context_data(**kwargs)

        return context


class Warning(TemplateView):

    template_name='notes/warning.html'

    def get_context_data(self,**kwargs):

        context=super().get_context_data(**kwargs)

        return context


    
    
    



    

    
