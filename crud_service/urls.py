
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from django.urls import path, include

from accounts import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('companies/', include('companies.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns