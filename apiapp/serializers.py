from django.db.models import Count
from rest_framework import serializers
from hqapp.models import Product, ProductWithStudent, Lesson, Student
from rest_framework.relations import SlugRelatedField


class StudentSerializer(serializers.ModelSerializer):
    """Сериализатор api для вывода списка студентов"""
    class Meta:
        model = Student
        fields = "pk", "name",


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор api для вывода списка уроков"""
    class Meta:
        model = Lesson
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор api для вывода списка продуктов"""
    lessons_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()
    percent = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    # students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "pk", "product_name", "lessons_count", "student_count", "percent", "lessons"#"total_time"

    def get_lessons_count(self, obj):
        result = Lesson.objects.filter(lesson=obj).aggregate(Count("lesson"))
        return result["lesson__count"]

    def get_student_count(self, obj):
        result = ProductWithStudent.objects.filter(product=obj).aggregate(Count('student'))
        return result["student__count"]

    def get_percent(self, obj):
        result = Student.objects.all().aggregate(Count("pk"))
        return round((self.get_student_count(obj) / result["pk__count"] * 100), 2)