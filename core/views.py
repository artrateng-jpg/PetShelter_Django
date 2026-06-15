from django.db.models import Count
from django.shortcuts import render

from pets.models import Pet, MedicalRecord
from staff.models import Specialist
from .models import AdoptionRequest


def index(request):
    active_pets = Pet.objects.filter(is_active=True)

    free_count = active_pets.filter(status=Pet.STATUS_AVAILABLE).count()
    adopted_count = active_pets.filter(status=Pet.STATUS_ADOPTED).count()
    reserved_count = active_pets.filter(status=Pet.STATUS_RESERVED).count()
    total_count = active_pets.count()
    new_requests_count = AdoptionRequest.objects.filter(
        status=AdoptionRequest.STATUS_NEW, is_active=True
    ).count()

    pets = (
        active_pets.filter(status=Pet.STATUS_AVAILABLE)
        .select_related("category", "curator")
    )

    specialists = (
        Specialist.objects.filter(is_active=True)
        .annotate(pets_count=Count("curated_pets"))
        .order_by("-pets_count")[:5]
    )

    medical_records = (
        MedicalRecord.objects.select_related("pet", "pet__category", "vet")
        .order_by("-created_at")[:10]
    )

    context = {
        "pets": pets,
        "specialists": specialists,
        "medical_records": medical_records,
        "stats": {
            "free": free_count,
            "adopted": adopted_count,
            "reserved": reserved_count,
            "total": total_count,
            "new_requests": new_requests_count,
        },
    }
    return render(request, "index.html", context)
