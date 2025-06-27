from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', views.resume, name='resume'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
]