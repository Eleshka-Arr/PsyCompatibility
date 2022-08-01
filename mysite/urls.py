from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MainApp.urls')),
    path('news/', include('news.urls')),
    path('ous/', include('ous.urls')),
    path('quiz/', include('quiz.urls')),
    path('users/', include('users.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
