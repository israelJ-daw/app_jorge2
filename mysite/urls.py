from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("alquiler.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/', include("alquiler.api_urls")),  
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),  
    ]
