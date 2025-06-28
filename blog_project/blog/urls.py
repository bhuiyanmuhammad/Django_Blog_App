from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/edit/<int:id>/', views.post_edit, name='post_edit'),
    path('post/delete/<int:id>/', views.post_delete, name='post_delete'),
]
