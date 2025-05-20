from django.urls import path
from account.views import auth

app_name = "account"

urlpatterns = [
    path("register/", auth.register, name="register"),
    path("login/", auth.login_view, name="login"),
    path("logout/", auth.logout_view, name="logout"),
    path("profile/", auth.profile_view, name="profile"),
    path("profile/edit/", auth.edit_profile, name="edit-profile"),
    path("profile/delete/", auth.delete_account, name="delete-account"),
]