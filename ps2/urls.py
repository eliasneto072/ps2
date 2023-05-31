from django.urls import path,include
from .views import homeView,jogosView


urlpatterns = [
    path('', homeView, name='home'),   
    path('jogos/<int:id>', jogosView, name='jogos'),   
]

