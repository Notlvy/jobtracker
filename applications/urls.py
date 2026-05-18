from django.urls import path
from . import views

# Setting up URL paths for the applications app.

urlpatterns = [
    path('', views.application_list, name='application_list'),
    path('add/', views.application_create, name='application_create'),
    path('<int:pk>/edit/', views.application_edit, name='application_edit'),
    path('<int:pk>/delete/', views.application_delete, name='application_delete'),
    path('export/', views.export_csv, name='export_csv'),
    path('<int:pk>/status/', views.application_status_update, name='application_status_update'),
]