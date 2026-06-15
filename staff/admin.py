from django.contrib import admin

from .models import Specialist


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ("full_name", "role", "phone", "is_active")
    list_filter = ("role", "is_active", "categories")
    search_fields = ("full_name", "phone")
    filter_horizontal = ("categories",)
