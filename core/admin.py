from django.contrib import admin

from .models import Category, AdoptionRequest


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)


@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "pet", "status", "is_active", "created_at")
    list_filter = ("status", "is_active", "created_at")
    search_fields = ("name", "phone")
    list_editable = ("status",)
