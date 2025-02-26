from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    if request.user.user_type == 'patient':
        return render(request, 'users/patient_dashboard.html', {'user': request.user})
    elif request.user.user_type == 'doctor':
        return render(request, 'users/doctor_dashboard.html', {'user': request.user})
    return redirect('login')







# Doctor - Create a Blog Post
@login_required
def create_blog_post(request):
    if request.user.user_type != 'doctor':
        return redirect('dashboard')

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('dashboard')
    else:
        form = BlogPostForm()
    return render(request, 'users/create_blog.html', {'form': form})

# Doctor - View Their Blog Posts
@login_required
def doctor_blog_posts(request):
    blogs = BlogPost.objects.filter(author=request.user)
    return render(request, 'users/doctor_blog_list.html', {'blogs': blogs})

# Patient - View Published Blog Posts by Category
@login_required
def patient_blog_posts(request):
    categories = ['mental_health', 'heart_disease', 'covid19', 'immunization']
    category_posts = {category: BlogPost.objects.filter(category=category, is_draft=False) for category in categories}
    
    return render(request, 'users/patient_blog_list.html', {'category_posts': category_posts})
