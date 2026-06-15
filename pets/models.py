from django.db import models


class Pet(models.Model):
    """Питомец приюта."""

    STATUS_AVAILABLE = "available"
    STATUS_RESERVED = "reserved"
    STATUS_ADOPTED = "adopted"
    STATUS_CHOICES = [
        (STATUS_AVAILABLE, "Свободен"),
        (STATUS_RESERVED, "Забронирован"),
        (STATUS_ADOPTED, "Пристроен"),
    ]

    name = models.CharField("Кличка", max_length=120)
    breed = models.CharField("Порода", max_length=100, blank=True)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Фото", upload_to="pets/", blank=True, null=True)
    category = models.ForeignKey(
        "core.Category",
        verbose_name="Категория",
        on_delete=models.PROTECT,
        related_name="pets",
    )
    curator = models.ForeignKey(
        "staff.Specialist",
        verbose_name="Куратор",
        on_delete=models.SET_NULL,
        related_name="curated_pets",
        null=True,
        blank=True,
    )
    age_months = models.PositiveIntegerField("Возраст (мес.)", default=0)
    status = models.CharField(
        "Статус", max_length=20, choices=STATUS_CHOICES, default=STATUS_AVAILABLE
    )
    is_active = models.BooleanField("Опубликован", default=True)
    arrived_at = models.DateField("Дата поступления", auto_now_add=True)

    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"
        ordering = ["-arrived_at", "-id"]

    def __str__(self):
        return self.name

    @property
    def is_adopted(self):
        return self.status == self.STATUS_ADOPTED


class MedicalRecord(models.Model):
    """Запись в медицинской карте питомца."""

    pet = models.ForeignKey(
        Pet,
        verbose_name="Питомец",
        on_delete=models.CASCADE,
        related_name="medical_records",
    )
    vet = models.ForeignKey(
        "staff.Specialist",
        verbose_name="Ветеринар",
        on_delete=models.SET_NULL,
        related_name="medical_records",
        null=True,
        blank=True,
    )
    diagnosis = models.CharField("Диагноз / процедура", max_length=255)
    notes = models.TextField("Заметки", blank=True)
    is_vaccinated = models.BooleanField("Вакцинирован", default=False)
    created_at = models.DateField("Дата записи", auto_now_add=True)

    class Meta:
        verbose_name = "Медицинская запись"
        verbose_name_plural = "Медицинские карты"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.pet.name} — {self.diagnosis}"
