from django import forms
from .models import Student, Course, Rating


class StudentRatesEditForm(forms.Form):
    student = forms.IntegerField(widget=forms.HiddenInput())
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    rate = forms.IntegerField()

