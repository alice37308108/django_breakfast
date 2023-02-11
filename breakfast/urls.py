from django.urls import path

from breakfast.views import IndexView, BreakfastListView, ItemDetailView, BreakfastCreateView

app_name = 'breakfast'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list/', BreakfastListView.as_view(), name='list'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', BreakfastCreateView.as_view(), name='create'),
]
