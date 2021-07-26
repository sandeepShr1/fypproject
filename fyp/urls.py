from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include


urlpatterns = [
    path('', include('houseprediction.urls') ),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls') ),
    path('house/', include('House.urls'))
  
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
