from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Publication
from django.urls import reverse_lazy


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
