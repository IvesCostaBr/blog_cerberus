from rest_framework import serializers
from ..models import Author
from forum.api.viewsets import UserViewSet

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    user = UserViewSet(many=True)
    class Meta:
        model = Author
        fields = [ 'id', 'user']