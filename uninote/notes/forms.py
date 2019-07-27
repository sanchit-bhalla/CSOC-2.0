from django import forms
from django.forms import CharField,ModelForm,ChoiceField,TextInput,Select
from .models import *



class GetNotes(ModelForm):


    department=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    subject=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}))


    class Meta:

        model=Subject

        fields=['semester','subject']



        widgets={
                   'semester':TextInput(attrs={'class':'form-control'})



            }



class Semester(forms.Form):

     SEMESTER=( ('first','First'),
           ('second','Second'),
           ('third','Third'),
           ('fourth','Fourth'),
           ('fifth','Fifth'),
           ('sixth','Sixth'),
           ('seventh','Seventh'),
           ('eigth','Eigth'),

        )

     department=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
     semester=forms.ChoiceField(choices=SEMESTER,widget=forms.Select(attrs={'class':'form-control'}))


class Choose(forms.Form):

     SEMESTER=( ('first','First'),
           ('second','Second'),
           ('third','Third'),
           ('fourth','Fourth'),
           ('fifth','Fifth'),
           ('sixth','Sixth'),
           ('seventh','Seventh'),
           ('eigth','Eigth'),

        )

     department=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}))
     semester=forms.ChoiceField(choices=SEMESTER,widget=forms.Select(attrs={'class':'form-control'}))




class AddPdffiles(ModelForm):

     class Meta:

       model=PdfFiles
       fields=['subject','files','image','term']


       widgets={
                    'term':Select(attrs={'class':'form-control'}),
                    'subject':Select(attrs={'class':'form-control'}),
                    


           }




class UpdatePdffiles(ModelForm):


     class Meta:

       model=PdfFiles
       fields=['subject','files','image','term']


       widgets={
                    'term':Select(attrs={'class':'form-control'}),
                    'subject':Select(attrs={'class':'form-control'})

           }
