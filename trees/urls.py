from django.urls import path
from . import views

app_name = 'trees'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tree-types/', views.tree_types, name='tree_types'),
    path('forest-facts/', views.forest_facts, name='forest_facts'),
    path('tree-care/', views.tree_care, name='tree_care'),
]