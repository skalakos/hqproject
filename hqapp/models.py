from django.db import models


class Author(models.Model):
    """Модель владельца видеоурока"""

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"

    name = models.CharField(max_length=100, verbose_name="name")


class Product(models.Model):
    """Модель товара"""

    class Meta:
        verbose_name_plural = ("products")
        verbose_name = ("product")

    author =  models.ForeignKey(
        Author, on_delete=models.CASCADE, verbose_name="author")
    lesson = models.ForeignKey(
        "Lesson", on_delete=models.CASCADE, related_name="lesson")


class Lesson(models.Model):
    """Модель урока"""

    STATUS_VIDEO = [
        ("True", "true"),
        ("False ", "false"),
    ]

    title = models.CharField(max_length=200, verbose_name="title")
    link = models.URLField(max_length=360, verbose_name="link")
    video_time = models.PositiveIntegerField()
    viewed = models.CharField(choices=STATUS_VIDEO, default="false")


