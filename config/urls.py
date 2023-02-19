from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('breakfast.urls')),
    path('admin/', admin.site.urls),
    # path('breakfast/', include('breakfast.urls')),
]
