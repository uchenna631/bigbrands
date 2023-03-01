from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete_post/<slug:slug>/', views.delete_post, name='delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
