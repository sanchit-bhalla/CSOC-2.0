from django import forms
from django.forms import CharField,ModelForm,ChoiceField,Select
from .models import *



class GetNotes(ModelForm):
    

    department=forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    subjects=[]
    for x in Subject.objects.all():

        subjects.append((x.subject,x.subject))
    CHOICES=subjects
    subject=forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs={'class':'form-control'}))

    
    class Meta:

        model=Notes

        fields=['year','subject']



        widgets={
                   'year':Select(attrs={'class':'form-control'})



            }

        
