from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views.generic import CreateView, ListView, DetailView
from .models import Publication, Comentario
from django.urls import reverse_lazy
from .forms import ComentarioForm



class PublicationList(ListView):
    model = Publication


class CreatePubli(CreateView):
    model = Publication
    fields = ['title', 'bio']
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user.author
        obj.save()
        return super(CreatePubli, self).form_valid(form)


class PublicationDetail(DetailView):
    model = Publication

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        form = ComentarioForm(self.request.POST)
        form.is_valid()
        form = form.cleaned_data
        coment = Comentario.objects.create(author=self.request.user.author,
        text=form['text'], publication=obj)
        coment.save()
        return redirect(reverse('detail_publi', args=[obj.id]))
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm
        context['lista_comments'] = Comentario.objects.lastComents()
        return context
