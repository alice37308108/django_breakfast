from django.urls import path

from breakfast.views import (IndexView,
                             BreakfastListView,
                             ItemDetailView,
                             BreakfastCreateView,
                             BreakfastFormView,
                             BreakfastUpdateView)

app_name = 'breakfast'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list/', BreakfastListView.as_view(), name='list'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', BreakfastCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BreakfastUpdateView.as_view(), name='update'),
    # path('create/', BreakfastFormView.as_view(), name='create'),
]
