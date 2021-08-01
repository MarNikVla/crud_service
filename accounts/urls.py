from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('registration/', views.RegisterUserFormView.as_view(), name='registration'),
    path('update/update_done/', views.ProfileUpdateDoneView.as_view(), name='update_done'),
    path('update/', views.ProfileUpdateView.as_view(), name='update_profile'),
    path('users/', views.ProfileListView.as_view(), name='users_list'),
    path('user/<int:pk>', views.ProfileDetailView.as_view(), name='user_detail'),
]
