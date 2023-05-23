from django.forms import ModelForm
from .models import Contacto

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['name', 'lastname', 'phone', 'mobile', 'email', 'company', 'notes']
    
    