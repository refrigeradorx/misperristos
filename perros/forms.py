from django import forms 
from .models import Post

class PostForm(forms.ModelForm):
  
    Nombre = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    Raza = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))   
    
    Descripcion = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
        }
    ))     

    Nombre = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))   
    
    

    class Meta:
        model = Post   
        fields = ('Nombre', 'Raza', 'Descripcion', 'Fotografia', 'Estado', )
