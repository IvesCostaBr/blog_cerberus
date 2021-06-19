from django import forms

class ComentarioForm(forms.Form):
    text = forms.CharField(max_length=15000, 
    label="Comentario",
    widget=forms.Textarea(attrs={'class':'form-control',
    'style':'width:600px; height:100px;'}))