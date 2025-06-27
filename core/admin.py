from django.contrib import admin
from .models import Post, Contact, Experience, Education


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'period', 'order', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'company']
    list_editable = ['order']
    ordering = ['order', '-created_at']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'school', 'period', 'order', 'created_at']
    list_filter = ['created_at']
    search_fields = ['degree', 'school']
    list_editable = ['order']
    ordering = ['order', '-created_at']
