from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework.views import APIView
from hqapp.models import Product, Student, Lesson
from .serializers import ProductSerializer, StudentSerializer, LessonSerializer

class AllProductsApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StudentApiView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "pk",


class LessonApiView(APIView):

    def get(self, request: Request) -> Response:
        queryset = Lesson.objects.all()
        serializer = LessonSerializer(queryset, many=True)
        return Response(list(serializer.data))
