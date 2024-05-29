from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customadmin import urls as customadmin_urls


from authority import urls as authority_urls



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('dashboard/',include('customadmin.urls')),
    path('', include('Clothing_Accounts.urls')),
    path('ClothingApp/', include('ClothingApp.urls')),
    path('authority/', include(authority_urls)),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
