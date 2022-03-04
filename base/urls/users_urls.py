from django.urls import path
from  base.views import  users_views as views



urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.registerUser, name='register'),

    path('profile/', views.getUserProfile, name='user_profile'),
    path('profile/update/', views.updateUserProfile, name='user_profile-update'),
    path('studentScores/', views.studentScores, name='studentScores'),

    path('', views.getUsers, name='users'),
    path('students/', views.students,name='students'),
    path('<str:pk>/', views.getUserById, name='user'),

    path('update/<str:pk>/', views.updateUser, name='user-update'),

    path('delete/<str:pk>/', views.deleteUser, name='user-delete'),

]