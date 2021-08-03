from django.urls import path

from . import views

app_name = 'companies'

urlpatterns = [
  path('', views.CompanyList.as_view(), name='company_list'),
  path('new/', views.CompanyCreate.as_view(), name='company_new'),
  path('edit/<int:pk>/', views.CompanyUpdateView.as_view(), name='company_edit'),
  path('delete/<int:pk>/', views.CompanyDelete.as_view(), name='company_delete'),
  path('company/<int:pk>', views.CompanyDetailView.as_view(), name='company_detail'),
]