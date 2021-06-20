
from django import shortcuts
from django import urls
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from .models import Author
from .forms import AuthorDataForm


class AuthorDetail(DetailView):
    model = Author



class UpdateDataAuthor(UpdateView):
    model = Author
    fields = ['description', 
        'instagram',
         'linkedin', 
         'github', 
         'curriculo',
         'telefone',
         'localization',
         'profile_photo']
    success_url = urls.reverse_lazy('homepage')
   

    
  



