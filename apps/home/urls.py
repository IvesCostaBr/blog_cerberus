from django.conf.urls import include
from django.urls import path
from .views import (
    HomePage,

)
from apps.publications import urls as urls_pub

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('publication/', include(urls_pub)),
    path('category/', include('apps.category.urls')),
]
