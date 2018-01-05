from django.urls import path
from . import views

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/album/id
    path('album/<int:album_id>/', views.detail, name='detail'),
]
