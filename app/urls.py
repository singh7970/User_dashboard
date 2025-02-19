from django.urls import path
from .views import signup, login_view, logout_view, dashboard

urlpatterns = [
    path('', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]
