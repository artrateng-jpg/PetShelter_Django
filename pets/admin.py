from django.contrib import admin

from .models import Pet, MedicalRecord


class MedicalRecordInline(admin.TabularInline):
    model = MedicalRecord
    extra = 0


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "curator", "age_months", "status", "is_active")
    list_filter = ("status", "is_active", "category")
    search_fields = ("name",)
    list_editable = ("status",)
    inlines = [MedicalRecordInline]


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ("pet", "diagnosis", "vet", "is_vaccinated", "created_at")
    list_filter = ("is_vaccinated", "created_at", "vet")
    search_fields = ("pet__name", "diagnosis")
