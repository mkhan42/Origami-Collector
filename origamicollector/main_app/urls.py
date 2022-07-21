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
    path('origami/<int:origami_id>/add_decoration/', views.add_decoration, name='add_decoration'),
    path('materials/', views.MaterialList.as_view(), name='materials_index'),
    path('materials/<int:pk>/', views.MaterialDetail.as_view(), name='materials_detail'),
    path('materials/create/', views.MaterialCreate.as_view(), name='materials_create'),
    path('materials/<int:pk>/update/', views.MaterialUpdate.as_view(), name='materials_update'),
    path('materials/<int:pk>/delete/', views.MaterialDelete.as_view(), name='materials_delete'),
    path('origami/<int:origami_id>/assoc_material/<int:material_id>/', views.assoc_material, name='assoc_material'),
]