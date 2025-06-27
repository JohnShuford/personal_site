from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        ordering = ['-created_at']


class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    period = models.CharField(max_length=50)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

    class Meta:
        ordering = ['order', '-created_at']


class Education(models.Model):
    degree = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    period = models.CharField(max_length=50)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.degree} from {self.school}"

    class Meta:
        ordering = ['order', '-created_at']
