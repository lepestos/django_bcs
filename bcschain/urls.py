from django.urls import path
from . import views


urlpatterns = [
    path('blocks/', views.BlockListView.as_view(),
         name='block_list'),
    path('blocks/<int:pk>/', views.BlockDetailView.as_view(),
         name='block_detail'),
]
