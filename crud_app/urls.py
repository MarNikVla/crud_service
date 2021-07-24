from django.urls import path

from crud_app import views
from crud_app.views import IndexView

app_name = 'shop'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('<slug:category_slug>/', views.product_list,
    # name='product_list_by_category'),
    # path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]