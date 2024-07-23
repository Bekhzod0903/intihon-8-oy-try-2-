from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import set_language

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('users/', include('users.urls')),
    path('set-language/', set_language, name='set_language'),  # Add this line
]
