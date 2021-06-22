from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from apps.publications.models import Publication
from django.views import View
from .forms import RegisterForm
from django.contrib.auth.models import User
from apps.author.models import Author
import json
from django.forms.models import model_to_dict


class HomePage(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_publication'] = Publication.objects.all().order_by('-id')[:7]
        return context


class Register(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm
        return render(self.request, 'registration/sigin.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(self.request.POST or None, self.request.FILES)

        form.is_valid()
        form = form.cleaned_data
        user = User.objects.create_user(
            form['username'],
            form['email'],
            form['password1'],
        )
        user.save()
        author = Author.objects.create(user=user)
        author.prfile_photo = form['photo']
        author.save()
        return redirect('login')
        

def getAjax(request):
    if request.is_ajax() and request.method == 'GET':
        valor = request.GET.get('id')
        print(valor)
        publication = Publication.objects.get(id=1)
        print(model_to_dict(publication))
        data = json.dumps({'list':'ives'})
        return HttpResponse(data, content_type='application/json')
    return JsonResponse({'type':'is not request of type AJAX'}, status=400)
