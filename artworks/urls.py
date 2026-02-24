from django.urls import path

from . import views

urlpatterns = [
    path("versions/", views.versions, name="versions"),
    path("create-instance/", views.create_instance, name="create_instance"),
    path("artwork/<uuid>/", views.artwork_instance, name="artwork_instance"),
    path("deactivate-instance/<uuid>/", views.deactivate_instance, name="deactivate_instance"),
    # The dashboard view is now only accessible at /dashboard/ (see project urls.py)
    path('', views.dashboard, name='dashboard'),
]
