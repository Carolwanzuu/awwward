from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.welcome,name = 'welcome'),
    path('profile/',views.Profile,name = 'profile'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
