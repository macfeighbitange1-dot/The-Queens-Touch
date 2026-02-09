from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # The Royal Admin Command Center
    path('admin/', admin.site.urls),
    
    # Your Services App (Home, etc.)
    path('', include('services.urls')),
]

# The "Image Pipeline" Logic
# This allows Django to serve the images you upload in the admin panel 
# while you are in development mode (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Also serving static files explicitly (good for local testing)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)