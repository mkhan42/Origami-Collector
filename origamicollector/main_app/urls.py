from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('origami/', views.origami_index, name='index'),
    path('origami/<int:origami_id>/', views.origami_detail, name='detail'),
    path('origami/create/', views.OrigamiCreate.as_view(), name='origami_create'),
    path('origami/<int:pk>/update/', views.OrigamiUpdate.as_view(), name='origami_update'),
    path('origami/<int:pk>/delete/', views.OrigamiDelete.as_view(), name='origami_delete'),
]