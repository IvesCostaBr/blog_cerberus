from apps.staff.views import HomeEquipe
from django.urls import path

urlpatterns = [
    path('equipe/', HomeEquipe.as_view(), name='equipe')
]
