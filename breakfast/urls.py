from django.contrib import admin
from django.urls import path, include

from breakfast.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
