from django import forms
from .models import *


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }


class KafedraForm(forms.ModelForm):
    class Meta:
        model = Kafedra
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }


class GuruhForm(forms.ModelForm):
    class Meta:
        model = Guruh
        fields = "__all__"
        widgets = {
            "faculty": forms.Select(attrs={'class': 'form-control'}),
            "name": forms.TextInput(attrs={'class': 'form-control'})
        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'})

        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "subjects": forms.SelectMultiple(attrs={'class': 'form-control'})
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "age": forms.NumberInput(attrs={'class': 'form-control'}),
            "guruh": forms.Select(attrs={'class': 'form-control'}),
            "img": forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
