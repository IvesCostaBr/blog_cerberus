from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from apps.publications.models import Publication
from django.views import View
from .forms import RegisterForm
from django.contrib.auth.models import User




class HomePage(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_publication'] = Publication.objects.all()
        return context


class Register(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm
        return render(self.request, 'registration/sigin.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        form.is_valid()
        form = form.cleaned_data
        user = User.objects.create_user(
            form['username'],
            form['email'],
            form['password1'],
        )
        user.save()
        return redirect('login')
        
