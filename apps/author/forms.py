from django import forms
from .models import Author

class AuthorDataForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['description', 
        'instagram',
         'linkedin', 
         'github', 
         'curriculo',
         'telefone',
         'profile_photo']