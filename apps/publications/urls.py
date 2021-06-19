from django.urls import path
from .views import (
    PublicationList,
    CreatePubli,
    PublicationDetail,
  
)


urlpatterns = [
    path('publication-list/', PublicationList.as_view(), name='pub_list'),
    path('create-publication/', CreatePubli.as_view(), name='pub_create'),
    path('publication-detail/<int:pk>/', PublicationDetail.as_view(), name='detail_publi'),
  
]
