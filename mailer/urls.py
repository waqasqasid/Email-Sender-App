from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('send-email/', views.send_email, name='send_email'),  # Send email page (protected)
    path('signup/', views.signup, name='signup'),  # Signup page (public)
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login page (public)
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout page
]