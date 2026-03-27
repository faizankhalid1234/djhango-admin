"""
URL configuration for myproject project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, about, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('accounts/', include('accounts.urls')),
    path('locations/', include('locations.urls')),
]

# Custom error pages
handler400 = "myproject.views.handler400"
handler403 = "myproject.views.handler403"
handler404 = "myproject.views.handler404"
handler500 = "myproject.views.handler500"

# Serve uploaded media files in development (Choose File uploads)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)