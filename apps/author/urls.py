from django.urls import path
from .views import (
    AuthorDetail,
    UpdateDataAuthor
)


urlpatterns = [
    path('user-config/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
    path('edit-user/<int:pk>/', UpdateDataAuthor.as_view(), name='update_user')
]
