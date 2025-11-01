from django.contrib import admin
from django.urls import path
from notes import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
     path("delete/<int:note_id>/", views.delete_note, name="delete_note"),
    path("edit/<int:note_id>/", views.edit_note, name="edit_note"),
]
