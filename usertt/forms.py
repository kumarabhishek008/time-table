from django.forms import ModelForm
from .models import timetablecolumn

class timetable_form(ModelForm):
    class Meta:
        model = timetablecolumn
        fields = ['row','c1','c2','c3','c4','c5','c6','c7','c8','c9']

class DeleteRow(ModelForm):
    class Meta:
        model = timetablecolumn
        fields = ['row']