from django.urls import path
from .views import AllProductsApiView, StudentListApiView, LessonApiView, StudentApiView


app_name = "apiapp"

urlpatterns = [
    path("products/", AllProductsApiView.as_view(), name='products_list'),
    path("students/", StudentListApiView.as_view(), name="students"),
    path("student/<int:pk>", StudentApiView.as_view(), name="student"),
    path("lessons/", LessonApiView.as_view(), name="lessons")

]