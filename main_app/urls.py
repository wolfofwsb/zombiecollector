from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('zombies/', views.zombies_index, name='index'),
  path('zombies/<int:zombie_id>/', views.zombies_detail, name='detail'),
  path('zombies/create/', views.ZombieCreate.as_view(), name='zombies_create'),
  path('zombies/<int:pk>/update/', views.ZombieUpdate.as_view(), name='zombies_update'),
  path('zombies/<int:pk>/delete/', views.ZombieDelete.as_view(), name='zombies_delete'),
  path('zombies/<int:zombie_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('zombies/<int:zombie_id>/assoc_wound/<int:wound_id>/', views.assoc_wound, name='assoc_wound'),


]

