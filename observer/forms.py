from django import forms
from .models import Student, Section, Group, Filial


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields = ('first_name', 'last_name', 'phone', 'ticket', 'filial', 'section', 'group')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['section'].queryset = Section.objects.none()
        self.fields['group'].queryset = Group.objects.none()

        if 'filial' in self.data:
            try:
                filial_id = int(self.data.get('filial'))
                self.fields['section'].queryset = Section.objects.filter(filial_id=filial_id).order_by('name')
                section_id = int(self.data.get('section'))
                self.fields['group'].queryset = Group.objects.filter(section_id=section_id).order_by('name')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['section'].queruset = self.instance.filial.section_set.order_by('name')
            self.fields['group'].queruset = self.instance.section.group_set.order_by('name')


class SectionForm(forms.ModelForm):
    class Meta:
        model=Section
        fields = ('name','filial')


class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields = ('name', 'filial', 'section')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['section'].queryset = Section.objects.none()

        if 'filial' in self.data:
            try:
                filial_id = int(self.data.get('filial'))
                self.fields['section'].queryset = Section.objects.filter(filial_id=filial_id).order_by('name')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['section'].queruset = self.instance.filial.section_set.order_by('name')


class FilialForm(forms.ModelForm):
    class Meta:
        model=Filial
        fields = ('name', 'phone', 'address')
