from django.urls import path
from  base.views import schools_views as views


urlpatterns = [
    path('', views.getSchools, name='schools'),
    path('create/', views.createSchool, name='create-create'),
    path('upload/', views.uploadImage, name='image-upload'),

    path('<str:pk>/', views.getSchool, name='school'),

    path('update/<str:pk>/', views.updateSchool, name='update-school'),
    path('delete/<str:pk>/', views.deleteSchool, name='delete-school'),

]