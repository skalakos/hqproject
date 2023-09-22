from django.db import models


class Author(models.Model):
    """Модель владельца видеоурока"""

    class Meta:
        verbose_name = "author"
        verbose_name_plural = "authors"

    name = models.CharField(max_length=100, verbose_name="name")

    def __str__(self) -> str:
        return f" {self.name}"


class Lesson(models.Model):
    """Модель урока"""

    # STATUS_VIDEO = [
    #     ("True", "true"),
    #     ("False ", "false"),
    # ]

    title = models.CharField(max_length=200, verbose_name="title")
    link = models.URLField(max_length=360, verbose_name="link")
    video_time = models.PositiveIntegerField()
    # viewed = models.CharField(choices=STATUS_VIDEO, max_length=30, default="false")
    # product = models.ManyToManyField(Product, related_name="lessons")

    def __str__(self) -> str:
        return f" {self.title}"


class Product(models.Model):
    """Модель товара"""

    class Meta:
        verbose_name_plural = ("products")
        verbose_name = ("product")

    author =  models.ForeignKey(
        Author, on_delete=models.CASCADE, verbose_name="author")
    product_name = models.CharField(max_length=300, verbose_name="product_name")
    lesson = models.ManyToManyField(Lesson, related_name="product")

    def __str__(self) -> str:
        return f"{self.product_name}"


class Student(models.Model):
    """Модель ученика"""

    STATUS_VIDEO = [
        ("True", "true"),
        ("False ", "false"),
    ]

    name = models.CharField(max_length=250, verbose_name="name")

    def __str__(self)-> str:
        return f"{self.name}"
