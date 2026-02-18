from django.urls import path
from . import views

urlpatterns = [
    path("versions/", views.versions, name="versions"),
]
