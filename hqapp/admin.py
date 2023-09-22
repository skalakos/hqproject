from django.contrib import admin
from django.db.models import Count
from hqapp.models import (
    Author,
    Lesson,
    Product,
    Student,
)


class ProductAuthorInLine(admin.TabularInline):
    model = Product


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        ProductAuthorInLine
    ]
    ordering = "pk",


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display_links = "pk", "product_name",
    list_display = "pk", "author", "product_name", "lessons", "count"
    ordering = "pk",

    def count(self, obj):
        result = Lesson.objects.filter(product=obj).aggregate(Count("product"))
        return result["product__count"]

    def lessons(self, obj):
        result = Lesson.objects.filter(product=obj).prefetch_related("product")
        return [i_lesson for i_lesson in result]


class ProductInLine(admin.TabularInline):
    model = Product.lesson.through


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [
        ProductInLine
    ]

    list_display = "pk", "title", "link", "video_time",
    list_display_links = "pk", "title",


@admin.register(Student)
class LessonAdmin(admin.ModelAdmin):
    list_display = "name",