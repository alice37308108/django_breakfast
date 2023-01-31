from django.contrib import admin
from django.urls import path, include

from breakfast.views import IndexView, BreakfastListView, ItemDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list/', BreakfastListView.as_view(), name='list'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
]
