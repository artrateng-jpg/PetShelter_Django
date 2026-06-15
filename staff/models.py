from django.db import models


class Specialist(models.Model):
    """Сотрудник приюта: ветеринар, куратор и т.д."""

    ROLE_VET = "vet"
    ROLE_CURATOR = "curator"
    ROLE_VOLUNTEER = "volunteer"
    ROLE_CHOICES = [
        (ROLE_VET, "Ветеринар"),
        (ROLE_CURATOR, "Куратор"),
        (ROLE_VOLUNTEER, "Волонтёр"),
    ]

    full_name = models.CharField("ФИО", max_length=200)
    image = models.ImageField("Фото", upload_to="staff/", blank=True, null=True)
    role = models.CharField(
        "Должность", max_length=20, choices=ROLE_CHOICES, default=ROLE_VET
    )
    phone = models.CharField("Телефон", max_length=30, blank=True)
    categories = models.ManyToManyField(
        "core.Category",
        verbose_name="Работает с категориями",
        related_name="specialists",
        blank=True,
    )
    is_active = models.BooleanField("Работает", default=True)

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"
        ordering = ["full_name"]

    def __str__(self):
        return f"{self.full_name} ({self.get_role_display()})"
