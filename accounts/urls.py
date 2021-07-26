from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', views.RegisterUserFormView.as_view(), name='registration'),
    path('update/update_done/', views.ProfileUpdateDoneView.as_view(), name='update_done'),
    path('update/', views.ProfileUpdateView.as_view(), name='update_profile'),
]
