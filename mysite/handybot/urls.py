from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:project_id>/", views.project_detail, name="project_detail"),
    path("<int:project_id>/suggestions/", views.suggestions, name="suggestions"),
    path("<int:project_id>/save_tools/", views.save_tools, name="save_tools"),
    path("<int:project_id>/list_saved/", views.list_saved, name="list_saved"),
]