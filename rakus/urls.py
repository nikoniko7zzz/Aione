from django.urls import path

from rakus import views

urlpatterns = [
    path("new/", views.raku_new, name="raku_new"),
    path("search/", views.raku_search, name="raku_search"),
    path("set/", views.raku_set, name="raku_set"),
    # path("<int:search_id>/", views.search_detail, name="search_detail"),
    # path("<int:search_id>/edit/", views.search_edit, name="search_edit"),
]
