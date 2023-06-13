from django import forms
from .models import Worker
from datetime import date

class Historyform(forms.Form):
    CHOICES = [(y.name,y.name) for x,y in enumerate(Worker.objects.all())]
    name = forms.ChoiceField(choices=CHOICES,label='Выберите сотрудника для отчета')
class Ondateform(forms.Form):
    date = forms.DateField(label='Выберите дату для отчета в формате YYYY-MM-DD')