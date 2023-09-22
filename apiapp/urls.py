from django.urls import path
from .views import AllProductsApiView, StudentApiView, LessonApiView


app_name = "apiapp"

urlpatterns = [
    path("products/", AllProductsApiView.as_view(), name='products_list'),
    path("students/", StudentApiView.as_view(), name="students"),
    path("lessons/", LessonApiView.as_view(), name="lessons")

]