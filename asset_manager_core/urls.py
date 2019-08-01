from django.contrib import admin
from django.urls import path, include

# from asset_manager import urls as asset_manager_urls

urlpatterns = [
    path("", include("asset_manager.urls")),
    path('admin/', admin.site.urls),
]
