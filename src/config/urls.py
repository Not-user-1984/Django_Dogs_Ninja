
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('dogs_api.urls')),
    path("api/v2/", include("dogs_api.v2.urls")),
]
