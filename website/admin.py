from django.contrib import admin
from .models import ContactUsQuery


@admin.register(ContactUsQuery)
class ContactUsQueryAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "phone_number",
        "email_address",
        "created_at",
    )

    list_filter = ("created_at",)
    search_fields = (
        "first_name",
        "last_name",
        "email_address",
        "phone_number",
    )

    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Contact Information", {
            "fields": (
                "first_name",
                "last_name",
                "phone_number",
                "email_address",
            )
        }),
        ("Message", {
            "fields": ("message",)
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
        }),
    )
