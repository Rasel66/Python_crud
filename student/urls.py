from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("home/", home),
    path("add_student/", add_student),
    path("delete-std/<int:roll>", delete_student),
    path("update-std/<int:roll>", update_student),
    path("do-update-std/<int:roll>", do_update_student)
]
