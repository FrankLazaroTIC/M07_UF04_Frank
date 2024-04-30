from django.forms import ModelForm
from .models import UsersTIC

class PersonaForm(ModelForm):
    class Meta:
        model = UsersTIC
        #fields = ['id', 'nom', 'cognoms', 'assignatures', 'rol']
        fields = '__all__'