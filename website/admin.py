from django.contrib import admin

from django.contrib import admin
from website.models import (
    ContactUsQuery,
    Category,
    Blog,
    Author
)


@admin.register(ContactUsQuery)
class ContactUsQueryAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email_address", "phone_number", "created_at")
    search_fields = ("first_name", "last_name", "email_address")
    list_filter = ("created_at",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_published", "created_at")
    list_filter = ("is_published", "category", "created_at")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("category",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','full_name', 'designation')

