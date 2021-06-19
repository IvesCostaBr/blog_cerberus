from ..models import Publication
from .Serializers import PublicationSerializer
from rest_framework import viewsets


class PublicationViewSet(viewsets.ModelViewSet):
   
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer