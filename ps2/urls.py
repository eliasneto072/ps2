from django.urls import path,include
from .views import homeView,featuresView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', homeView, name='home'),   
    path('features/', featuresView, name='features'),   
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)