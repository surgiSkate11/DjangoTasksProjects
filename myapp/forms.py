from django import forms


class CreateTaskForm(forms.Form):
    
    title = forms.CharField(label = 'Titulo de tarea: ', max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    
    description = forms.CharField(label = 'Descripcion de tarea: ', widget = forms.Textarea(attrs={'class': 'input'}), max_length=200, required = False)
    
    
class CreateNewProject(forms.Form):
    
    name = forms.CharField(label = 'Nombre del proyecto: ', max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    