from django.urls import path

from . import views

urlpatterns = [
    path("", views.load_links, name="links"),
    path("links", views.scrap_link, name="scrap_link"),
    path("links/<int:category_id>", views.show_links, name="show_links")
]