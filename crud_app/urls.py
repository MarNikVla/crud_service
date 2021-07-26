from django.urls import path

from crud_app import views
from crud_app.views import IndexView
from django.contrib.auth import views as auth_views

app_name = 'crud_app'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', views.RegisterUserFormView.as_view(), name='registration'),
    path('update/update_done/', views.ProfileUpdateDoneView.as_view(), name='update_done'),
    path('update/', views.ProfileUpdateView.as_view(), name='update_profile'),
]