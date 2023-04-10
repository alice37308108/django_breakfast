from breakfast import views
from django.urls import path

from breakfast.views import (IndexView,
                             BreakfastListView,
                             ItemDetailView,
                             BreakfastCreateView,
                             BreakfastUpdateView,
                             BreakfastDeleteView,
                             ContactListView,)

app_name = 'breakfast'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('list/', BreakfastListView.as_view(), name='list'),
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', BreakfastCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BreakfastUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BreakfastDeleteView.as_view(), name='delete'),
    path('tag/<slug:tag>/', BreakfastListView.as_view(), name='tag'),
    path('page_list', ContactListView.as_view(), name='page_list'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('user/', views.user_view, name='user'),
    path('other/', views.other_view, name='other'),
    # path('create/', BreakfastFormView.as_view(), name='create'),
]
