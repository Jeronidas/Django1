from django import forms 

class CrearAutoFormulario(forms.Form):
    marca = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    anio = forms.IntegerField()
    

class BuscarAutoFormulario(forms.Form):
    marca = forms.CharField(max_length=20, required=False)
    modelo = forms.CharField(max_length=20, required=False)