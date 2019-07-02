from django.db import models


    
class Departments(models.Model):

    
    dept=models.CharField(max_length=100,primary_key=True)
    HOD=models.CharField(max_length=100,blank=True,null=True)

    class Meta:

        
        verbose_name_plural='Departments'
        

    def __str__(self):

         return self.dept


        

class Subject(models.Model):

    department=models.ForeignKey(Departments,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100,blank=True,null=True)


    class Meta:

        
        verbose_name_plural='Subjects'

    def __str__(self):

        return self.subject
        

    
        

class PdfFiles(models.Model):

    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    files=models.FileField(upload_to='notes/myfiles',null=True,blank=True)
    image=models.ImageField(upload_to='myimages',null=True,blank=True)


    class Meta:

        
        verbose_name_plural='Pdffiles'

    def __str__(self):

        return self.subject.subject

    
    
    
class Notes(models.Model):

    YEAR=( ('first','First'),
           ('second','Second'),
           ('third','Third'),
           ('fourth','Fourth'),
        )

    department=models.ForeignKey(Departments,on_delete=models.CASCADE)
    year=models.CharField(max_length=20,choices=YEAR)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    files=models.ManyToManyField(PdfFiles)
    

    class Meta:

        
        verbose_name_plural='Notes'



    def __str__(self):

        return self.subject.subject

    
    
        




    
