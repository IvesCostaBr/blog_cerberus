from django.contrib import admin
from django.urls import path, include
from apps.home import urls as home_urls
from rest_framework import routers
from apps.publications.api import viewsets
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import urls as django_urls
from django.contrib.auth import views 
from apps.home.views import Register


router = routers.DefaultRouter()
router.register(r'publications', viewsets.PublicationViewSet, basename='publications')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)), 
    # path(),
    path('register/',Register.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
    path('user/', include('apps.author.urls')),
    path('login/',views.LoginView.as_view(), name='login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
