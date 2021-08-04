from django.urls import path

from searchs import views

urlpatterns = [
    path("new/", views.search_new, name="search_new"),
    path("<int:search_id>/", views.search_detail, name="search_detail"),
    path("<int:search_id>/edit/", views.search_edit, name="search_edit"),
]
