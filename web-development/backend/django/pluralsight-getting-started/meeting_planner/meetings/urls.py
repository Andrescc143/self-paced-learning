from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.detail, name='detail'),
    path('rooms', views.rooms, name='rooms')
]