from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator

deptset=Departments.objects.all()

def homepage(request):

    global deptset
    
    deptset=Departments.objects.all()
    paginator=Paginator(deptset,6)

    page=request.GET.get('page')

    depts=paginator.get_page(page)

    dept_set=depts.object_list
    
    form=Semester(auto_id=True)
    return render(request,template_name='papers/home.html',context={'deptset_range':list(zip(dept_set,list(range(len(dept_set))))),'form':form,'depts':depts})


def getpapers(request):

    global deptset


    department1=request.GET['department']
    semester=request.GET['semester']

    flag=0

    for x in Departments.objects.all():

        if x.dept==department1:

            flag=1
            break

    if flag==1:

      dept_subjects=Subject.objects.all().filter(Q(department__dept=department1),Q(semester=semester))

      if len(dept_subjects)==0:  

          return HttpResponseNotFound('Wait for the Files to be Uploaded to the Server')
        
      else:
      
          subjects=[]
      
          for x in dept_subjects:

               subjects.append(x.subject)

          CHOICES=subjects
      
          form=GetPapers(initial={'department':department1,'semester':semester},auto_id=True)
          form.fields['subject'].choices=[(choice,choice) for choice in CHOICES]
      
          return render(request=request,template_name='papers/getpapers.html',context={'form':form,'deptset':deptset})

    else:

         return HttpResponseRedirect('invalid/')


def displaypapers(request):

    global deptset

    dept=request.GET['department'].replace('+','%20')
    sub=request.GET['subject']

    queryset=Papers.objects.all()
    queryset=queryset.filter(Q(department__dept=dept),Q(subject__subject=sub))
    if len(queryset)==0:

        return HttpResponseRedirect('invalid/')

    else:
                             
       subject_notes=queryset[0]

       d={}
       d['department']=subject_notes.department.dept
       d['subject']=subject_notes.subject.subject
       file_list=[]

       for f in subject_notes.files.all():

           if f.files.name is '':
               
               return HttpResponseRedirect('warning/')
                

           else:
               
              file_name=f.files.name.replace('notes/myfiles/','')
              file_name=file_name.replace('.pdf','')
              file_list.append((f.files.url,f.image.url,file_name,f.term))

       d['files']=file_list

       files_minor1=list(filter(lambda x:(x[3]=='minor1'),d['files']))

       d['files1']=files_minor1

       files_minor2=list(filter(lambda x:(x[3]=='minor2'),d['files']))

       d['files2']=files_minor2

       files_major=list(filter(lambda x:(x[3]=='major'),d['files']))

       d['files3']=files_major


       return render(request=request,template_name='papers/displaypapers.html',context={'mydata':d,'deptset':deptset})


class InvalidRequest(TemplateView):

    template_name='papers/warning_page.html'

    def get_context_data(self,**kwargs):

        context=super().get_context_data(**kwargs)

        return context


class Warning(TemplateView):

    template_name='papers/warning.html'

    def get_context_data(self,**kwargs):

        context=super().get_context_data(**kwargs)

        return context
