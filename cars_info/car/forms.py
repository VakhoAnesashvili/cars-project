from django import forms 
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        

class CarFilterForm(forms.Form):

    search = forms.CharField(required=False) 