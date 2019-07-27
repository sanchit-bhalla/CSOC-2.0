from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q
from django.http import *
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required,user_passes_test
from django.template.defaulttags import register



@register.filter
def get_range(value):

    return range()


deptset=Departments.objects.all()


def homepage(request):

    global deptset


    deptset=Departments.objects.all()

    paginator=Paginator(deptset,6)

    page=request.GET.get('page')

    depts=paginator.get_page(page)

    dept_set=depts.object_list

    form=Semester(auto_id=True)

    return render(request=request,template_name='notes/home.html',context={'deptset_range':list(zip(dept_set,list(range(len(dept_set))))),'form':form,'depts':depts})
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


    sub=request.GET['subject']

    queryset=PdfFiles.objects.all()

    queryset=queryset.filter(subject__subject=sub)

    if len(queryset)==0:

        return HttpResponseRedirect('invalid/')

    else:

       subject_file_list=list(queryset)
       d={}
       file_list=[]
       for x in subject_file_list:
            if x.files.name is '':
                 return HttpResponseRedirect('warning/')

            else:

                 file_name=x.files.name.replace('notes/myfiles/','')
                 file_name=file_name.replace('.pdf','')
                 file_list.append((x.files.url,x.image.url,file_name,x.term))

       d['files']=file_list
       
       #####################################################################################
       files_minor1=list(filter(lambda x:(x[3]=='minor1'),d['files']))

       if len(files_minor1)==0:

           d['msg1']='Files will be uploaded soon'
           
       else:

           d['files1']=files_minor1
       #####################################################################################
       files_minor2=list(filter(lambda x:(x[3]=='minor2'),d['files']))

       if len(files_minor2)==0:

           d['msg2']='Files will be uploaded soon'
           
       else:

           d['files2']=files_minor2
       #####################################################################################
       files_major=list(filter(lambda x:(x[3]=='major'),d['files']))

       if len(files_major)==0:

           d['msg3']='Files will be uploaded soon'
           
       else:

           d['files3']=files_major
       #####################################################################################

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


@login_required
@user_passes_test(lambda u:u.is_superuser,login_url='/notes/')
def ChooseDeptForm(request):

   form=Choose()

   departments=Departments.objects.all()

   dept_list=[]

   for x in departments:

       dept_list.append(x.dept)

   CHOICES=dept_list

   form.fields['department'].choices=[(choice,choice) for choice in CHOICES]

   return render(request=request,template_name='notes/chooseform.html',context={'form':form})


@login_required
@user_passes_test(lambda u:u.is_superuser,login_url='/notes/')
def AddFilesForm(request):

   if request.method=='POST':

       form=AddPdffiles(request.POST,request.FILES)
       if form.is_valid():

           new_file=form.save()

           return HttpResponseRedirect('displayfiles')

   else:

       if request.GET=={}:

           return HttpResponseRedirect('choosedeptform')
        
       else:
            
            department=request.GET['department']
            semester=request.GET['semester']
            dept_subjects=Subject.objects.all().filter(Q(department__dept=department),Q(semester=semester))
            if len(dept_subjects)==0:
           
                return HttpResponseNotFound('Subjects not added')

            else:
           
              form=AddPdffiles()
              form.fields['subject'].queryset=Subject.objects.all().filter(Q(department__dept=department),Q(semester=semester))
              return render(request=request,template_name='notes/addfiles.html',context={'form':form})



@login_required
@user_passes_test(lambda u:u.is_superuser,login_url='/notes/')
def DisplayFiles(request):

    query_files=PdfFiles.objects.all()

    if len(query_files)==0:

        return HttpResponseNotFound('files not present')

    else:

      file_list=[]

      for x in query_files:

          file_name=x.files.name.replace('notes/myfiles/','')
          file_name=file_name.replace('.pdf','')

          file_list.append((x.id,x.subject.subject,x.subject.department.dept,x.subject.semester,x.term,file_name))

      paginator=Paginator(file_list,4)

      page=request.GET.get('page')

      files=paginator.get_page(page)

      file_list_set=files.object_list

      return render(request=request,template_name='notes/displayfiles.html',context={'file_list':file_list_set,'files':files})


@login_required
@user_passes_test(lambda u:u.is_superuser,login_url='/notes/')
def DeleteFiles(request):

    my_id=request.GET['id']

    del_obj=PdfFiles.objects.all().get(pk=my_id)

    del_obj.delete()

    return HttpResponseRedirect('displayfiles')


@login_required
@user_passes_test(lambda u:u.is_superuser,login_url='/notes/')
def UpdateFilesForm(request,id):

    if request.method=='POST':

        file_obj_old=PdfFiles.objects.all().get(pk=id)
        form=UpdatePdffiles(request.POST,request.FILES,instance=file_obj_old)
        if form.is_valid():

            file_obj_new=form.save()
            return HttpResponseRedirect('/notes/displayfiles')
    else:

        file_obj=PdfFiles.objects.all().get(pk=id)
        subject=file_obj.subject
        files=file_obj.files
        image=file_obj.image
        term=file_obj.term
        form=UpdatePdffiles(initial={'subject':subject,'files':files,'image':image,'term':term})
        return render(request=request,template_name='notes/updatefiles.html',context={'form':form,'id':id})
