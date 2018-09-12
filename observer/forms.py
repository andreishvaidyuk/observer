from django import forms
from .models import Student, Section, Group, Filial


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = ('first_name', 'last_name', 'phone', 'ticket', 'filial', 'section', 'group')


class SectionForm(forms.ModelForm):
    class Meta:
        model=Section
        fields = ('name','filial')


class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields = ('name', 'filial', 'section')


class FilialForm(forms.ModelForm):
    class Meta:
        model=Filial
        fields = ('name', 'phone', 'address')
