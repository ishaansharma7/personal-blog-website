from django.urls import path
from home_app import views

app_name = 'home_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('feed/', views.FeedView.as_view(), name='feed'),
    path('search/', views.search, name='search'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='detail_post'),
]
