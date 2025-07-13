from django.urls import path
from . import views
from django.shortcuts import redirect


urlpatterns = [
    path('home/',views.home, name="home"),
    path('login/',views.login_view, name="login"),
    path('logout/',views.logout_view, name="logout"),
    path('register/',views.register_view, name="register"),
    path('post/', views.add_post, name="add_post"),
    path('display/', views.post_show, name='show_post'),
    path('profile/', views.profile, name="profile"),
    path('post/delete/<int:pk>/', views.post_delete, name='delete_post'),
    path('post/edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('', lambda request: redirect('home')),

]