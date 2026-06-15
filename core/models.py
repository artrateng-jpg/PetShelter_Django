from django.db import models


class Category(models.Model):
    """Вид/категория животного: собаки, кошки и т.д."""

    name = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", blank=True)
    is_active = models.BooleanField("Активна", default=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class AdoptionRequest(models.Model):
    """Заявка на усыновление, оставленная посетителем сайта."""

    STATUS_NEW = "new"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_DONE = "done"
    STATUS_REJECTED = "rejected"
    STATUS_CHOICES = [
        (STATUS_NEW, "Новая"),
        (STATUS_IN_PROGRESS, "В работе"),
        (STATUS_DONE, "Завершена"),
        (STATUS_REJECTED, "Отклонена"),
    ]

    name = models.CharField("Имя заявителя", max_length=150)
    phone = models.CharField("Телефон", max_length=30)
    pet = models.ForeignKey(
        "pets.Pet",
        verbose_name="Питомец",
        on_delete=models.CASCADE,
        related_name="requests",
        null=True,
        blank=True,
    )
    message = models.TextField("Сообщение", blank=True)
    status = models.CharField(
        "Статус", max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW
    )
    is_active = models.BooleanField("Активна", default=True)
    created_at = models.DateTimeField("Создана", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка на усыновление"
        verbose_name_plural = "Заявки на усыновление"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Заявка
