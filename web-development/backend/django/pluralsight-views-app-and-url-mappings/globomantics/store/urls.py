from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    re_path(r'^logout', views.logout, name='logout'),
    re_path(r'^electronics', views.electronics, name='electronics'),
    re_path(r'^classview/electronics', views.ElectronicsView.as_view(), name='electronics_classview'),
]
