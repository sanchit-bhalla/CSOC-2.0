from django.db import models

class Departments(models.Model):

    dept=models.CharField(max_length=100,primary_key=True)
    HOD=models.CharField(max_length=100,blank=True,null=True)
    image=models.ImageField(upload_to='myimages',null=True,blank=True)

    class Meta:

        
        verbose_name_plural='Departments'
        

    def __str__(self):

         return '{}, {}'.format(self.dept,self.HOD)


class Subject(models.Model):

    SEMESTER=( ('first','First'),
           ('second','Second'),
           ('third','Third'),
           ('fourth','Fourth'),
           ('fifth','Fifth'),
           ('sixth','Sixth'),
           ('seventh','Seventh'),
           ('eigth','Eigth'),
           
        )

    department=models.ForeignKey(Departments,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100,blank=True,null=True)
    semester=models.CharField(max_length=20,choices=SEMESTER,blank=True,null=True)

    class Meta:

        
        verbose_name_plural='Subjects'

    def __str__(self):

        return '{},{},{} sem'.format(self.subject,self.department.dept,self.semester)
    

class PdfFiles(models.Model):

    TERM=[('minor1','minor1'),
          ('minor2','minor2'),
          ('major','major'),
        ]

    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    files=models.FileField(upload_to='notes/myfiles',default=1)
    image=models.ImageField(upload_to='myimages',null=True,blank=True)
    term=models.CharField(max_length=20,choices=TERM,default=1)


    class Meta:

        
        verbose_name_plural='Pdffiles'

    def __str__(self):

        return '{},{} sem,{}'.format(self.subject.subject,self.subject.semester,self.term)


##class Papers(models.Model):
##
##
##    department=models.ForeignKey(Departments,on_delete=models.CASCADE)
##    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
##    files=models.ManyToManyField(PdfFiles)
##    
##
##    class Meta:
##
##        
##        verbose_name_plural='Papers'
##
##
##
##    def __str__(self):
##
##         return '{},{}'.format(self.subject.subject,self.department.dept)
##
##
    
