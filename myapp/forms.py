from django import forms
from .models import Project

class CreateNewTask(forms.Form):
    class Meta:
        model = Project
        fields = ('title')
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    title = forms.CharField(label="Titulo de tarea", max_length=67, widget=forms.TextInput(attrs={'class':'input'}))
    description=forms.CharField(label="Descripcion de la tarea",widget=forms.Textarea(attrs={'class': 'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))