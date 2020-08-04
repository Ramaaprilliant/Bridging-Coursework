from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_list, name='cv_list'),
    path('<int:pk>/edit/', views.cv_edit, name='cv_edit'),
    path('new/', views.cv_new, name='cv_new'),
]