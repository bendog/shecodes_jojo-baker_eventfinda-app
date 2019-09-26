from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path("register/", views.Register.as_view(), name="register"),
    # event-finder/edit-profile
    path("editprofile/", views.EditProfile.as_view(), name="editprofile"),
]
