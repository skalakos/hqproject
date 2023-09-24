from django.db.models import Count
from rest_framework import serializers
from hqapp.models import Product, LessonViewed, Lesson, Student
from rest_framework.relations import SlugRelatedField


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор api для вывода списка уроков"""

    class Meta:
        model = Lesson
        fields = '__all__'

class LessonViewedSerializer(serializers.ModelSerializer):
    """Сериализатор api для вывода списка просмотренных уроков"""

    class Meta:
        model = LessonViewed
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор api для вывода списка продуктов"""
    lessons_count = serializers.SerializerMethodField()
    students_count = serializers.SerializerMethodField()
    percent = serializers.SerializerMethodField()
    viewed_lessons = serializers.SerializerMethodField()
    # students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "pk", "product_name", "lessons_count", "students_count", "percent", "viewed_lessons"#"total_time"

    def get_lessons_count(self, obj):
        result = Lesson.objects.filter(lesson=obj).aggregate(Count("lesson"))
        return result["lesson__count"]

    def get_students_count(self, obj):
        result = Student.objects.filter(products=obj).aggregate(Count('products'))
        return result["products__count"]

    def get_percent(self, obj):
        result = Student.objects.all().aggregate(Count("pk"))
        return round((self.get_students_count(obj) / result["pk__count"] * 100), 2)

    def get_viewed_lessons(self, obj):
        result = Lesson.objects.filter(lesson=obj).filter(lessons__viewed="True").aggregate(Count("lessons__viewed"))
        return result["lessons__viewed__count"]


class StudentSerializer(serializers.ModelSerializer):
    """Сериализатор api для вывода списка студентов"""
    # products = serializers.SerializerMethodField()
    products = ProductSerializer(many=True)
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = "pk", "name", "lessons", "products"

    def get_lessons(self, obj):
        result = LessonViewed.objects.filter(lessons=obj).select_related("lessons__student")
        return result