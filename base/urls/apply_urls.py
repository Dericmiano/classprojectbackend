from django.urls import path
from base.views import apply_views as views



urlpatterns = [
    path('', views.getApplications, name='applications'),
    # path('', views.getTest, name='applications'),

    # path('', views.successApplication, name='applications'),
    path('add/',views.addApplicationItems,name='application-add'),
    path('<str:pk>/', views.getApplicatioById, name='user-application'),

    path('app/<str:pk>/', views.getApplicationItemById, name='user-application'),

    # path('<str:pk>/', views.getApplicatioById, name='user-application'),

]