from django.urls import path

from blog import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('<str:title>/', views.BlogListView.as_view(), name='blog_category'),
    path('detail/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
]
