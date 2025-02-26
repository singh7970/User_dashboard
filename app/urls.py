from django.urls import path
from .views import signup, login_view, logout_view, dashboard
from .views import create_blog_post, doctor_blog_posts, patient_blog_posts
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create_blog/', create_blog_post, name='create_blog'),
    path('doctor_blogs/', doctor_blog_posts, name='doctor_blog_posts'),
    path('patient_blogs/', patient_blog_posts, name='patient_blog_posts'),

]





if settings.DEBUG:  # Only serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

