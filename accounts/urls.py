from django.urls import path
from .views import login_view, home_view, register_view, delete_post_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('delete/<int:post_id>/', delete_post_view, name='delete_post'),
    path('', home_view, name='home'),
]
