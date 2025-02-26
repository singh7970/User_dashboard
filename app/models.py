from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.username






from django.contrib.auth import get_user_model

User = get_user_model()

# Blog Category Model
def blog_image_path(instance, filename):
    return f'blog_images/{filename}'  # Ensures images are saved in media/blog_images/

class BlogCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Blog Post Model
class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('mental_health', 'Mental Health'),
        ('heart_disease', 'Heart Disease'),
        ('covid19', 'Covid19'),
        ('immunization', 'Immunization')
    ]
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=blog_image_path) 
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def truncated_summary(self):
        words = self.summary.split()
        return ' '.join(words[:15]) + '...' if len(words) > 15 else self.summary

    def __str__(self):
        return self.title
