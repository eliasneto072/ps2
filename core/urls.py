from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
    path('home/', include('ps2.urls')),
]
