from django.contrib import admin
from django.db.models import Count
from hqapp.models import (
    Author,
    Lesson,
    Product,
    Student,
    ProductWithStudent,
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
    list_display = "pk", "author", "product_name", "lessons", "count_lessons"
    ordering = "pk",

    def count_lessons(self, obj):
        result = Lesson.objects.filter(lesson=obj).aggregate(Count("lesson"))
        return result["lesson__count"]

    def lessons(self, obj):
        result = Lesson.objects.filter(lesson=obj).prefetch_related("lesson")
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


class ProductStudentInLine(admin.TabularInline):
    model = ProductWithStudent

#
# class LessonStudentInLine(admin.TabularInline):
#     model = Student.lessons.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [
        ProductStudentInLine,
        # LessonStudentInLine
    ]

    list_display = "pk", "name", "products", "lessons_for_student"
    ordering = "pk",

    def products(self, obj) -> str:
        result = Product.objects.filter(products=obj).aggregate(Count("products"))
        return result['products__count']

    def lessons_for_student(self, obj):
        result = Lesson.objects.filter(lesson=obj).prefetch_related("lesson")
        return [i_lesson for i_lesson in result]
