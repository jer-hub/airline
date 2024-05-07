from django.urls import path
from .views import index, add_flight, delete_flight, update_flight

app_name = "flight"
urlpatterns = [
    path("", index, name="index"),
    path("add_flight/", add_flight, name="add_flight"),
    path("delete_flight/<int:id>", delete_flight, name="delete_flight"),
    path("update_flight/<int:id>", update_flight, name="update_flight"),
]