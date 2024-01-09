from django.forms import ModelForm
from .models import studentdetails,MarkList
from django import forms

class StudentForm(ModelForm):
    class Meta:
        model = studentdetails
        fields = ['sregno','sname','sgender','sage','sdept','simage']
        labels = {'sregno':'Reg No','sname':'Name','sgender':'Gender','sage':'Age','sdept':'Department','simage':'Image'}
        """
        widgets = {
            'sgender': forms.RadioSelect(choices=studentdetails.GENDER_CHOICES)
        }
        """

"""
class MarkForm(ModelForm):
    class Meta:
        model = MarkList
        fields = ['date','sub1','mark1','sub2','mark2','sub3','mark3','sub4','mark4','sub5','mark5']
        labels = {'date':'Date of Exam','sub1':'Subject 1','mark1':'Marks','sub2':'Subject 2','mark2':'Marks','sub3':'Subject 3','mark3':'Marks','sub4':'Subject 4','mark4':'Marks','sub5':'Subject 5','mark5':'Marks'}
"""