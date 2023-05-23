from django.forms import ModelForm, DateInput
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'estimated_end', 'priority', 'done']
        widgets = { 'estimated_end': DateInput(attrs={'type': 'date'}) }