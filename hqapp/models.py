from django.db import models


class Profile(models.Model):
    pass


class Product(models.Model):
    """Модель товара"""

    # AVAILABLE_CHOICES = [
    #     ("true", _("true")),
    #     ("false ", _("false")),
    # ]

    class Meta:
        verbose_name_plural = ("products")
        verbose_name = ("product")

    user =  models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name="user")


class Lesson(models.Model):
        """Модель урока"""

        class Meta:
            verbose_name_plural = "lessons"
            verbose_name = "lesson"

    title = models.CharField(max_length=200, verbose_name='lesson')
