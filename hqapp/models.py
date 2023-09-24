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

    title = models.CharField(max_length=200, verbose_name="title")
    link = models.URLField(max_length=360, verbose_name="link")
    video_time = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f" {self.title}"


class Product(models.Model):
    """Модель товара"""

    class Meta:
        verbose_name_plural = "products"
        verbose_name = "product"

    author =  models.ForeignKey(
        Author, on_delete=models.CASCADE, verbose_name="author")
    product_name = models.CharField(max_length=300, verbose_name="product_name")
    lesson = models.ManyToManyField(Lesson, related_name="lesson")
    # student = models.ManyToManyField("Student", related_name="student")

    def __str__(self) -> str:
        return f"{self.product_name}"


class Student(models.Model):
    """Модель ученика"""

    name = models.CharField(max_length=250, verbose_name="name")
    products = models.ManyToManyField(Product, related_name="products")

    def __str__(self) -> str:
        return f"{self.name}"


class LessonViewed(models.Model):
    """Модель описывающая отношение продукта к ученику"""

    STATUS_VIDEO = [
        ("True", "true"),
        ("False ", "false"),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student")
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="lessons")
    viewed = models.CharField(choices=STATUS_VIDEO, max_length=32, default="false")
    viewed_time = models.PositiveIntegerField()