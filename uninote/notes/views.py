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
    form=Semester(auto_id=True)

    return render(request=request,template_name='notes/home.html',context={'deptset_range':list(zip(deptset,list(range(len(deptset))))),'form':form})
    #return render(request=request,template_name='notes/home.html',context={'deptset':deptset,'form':form})

    

    
def getnotes(request):

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

          return HttpResponseNotFound('Wait For the files to be uploaded to the server')
      else:
          
         subjects=[]
      
         for x in dept_subjects:

             subjects.append(x.subject)

         CHOICES=subjects
      
         form=GetNotes(initial={'department':department1,'semester':semester},auto_id=True)
         form.fields['subject'].choices=[(choice,choice) for choice in CHOICES]
      
         return render(request=request,template_name='notes/getnotes.html',context={'form':form,'deptset':deptset})

    else:

         return HttpResponseRedirect('invalid')
        

def displaynotes(request):

    global deptset

    dept=request.GET['department'].replace('+','%20')
    sub=request.GET['subject']

    queryset=Notes.objects.all()
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


    
    
    



    

    
