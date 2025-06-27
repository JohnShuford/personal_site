from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Post, Contact, Experience, Education
from .forms import ContactForm


def home(request):
    """Homepage view"""
    return render(request, 'core/home.html')


def resume(request):
    """Resume page with timeline"""
    experience = Experience.objects.all()
    education = Education.objects.all()
    
    context = {
        'experience': experience,
        'education': education
    }
    return render(request, 'core/resume.html', context)


def blog(request):
    """Blog list view"""
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'core/blog.html', {'posts': posts})


def blog_detail(request, slug):
    """Blog detail view"""
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'core/blog_detail.html', {'post': post})


def contact(request):
    """Contact form view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})
