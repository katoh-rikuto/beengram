import django.contrib.auth.views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path(
        "", TemplateView.as_view(template_name="main/index.html"), name="index"
    ),
    path("home/", views.PostListView.as_view(), name="home"),
    path(
        "settings/",
        TemplateView.as_view(template_name="main/settings.html"),
        name="settings",
    ),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path(
        "signup_email_send/",
        TemplateView.as_view(
            template_name="registration/signup_email_send.html"
        ),
        name="signup_email_send",
    ),
    path("activate/<token>/", views.ActivateView.as_view(), name="activate"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post_detail"),
    path("post/", views.PostView.as_view(), name="new_post"),
    path(
        "delete_post/<int:pk>",
        views.PostDeleteView.as_view(),
        name="delete_post",
    ),
    path("profile/<int:pk>", views.ProfileView.as_view(), name="profile"),
    path(
        "profile/follow-list/<int:pk>",
        views.FollowListView.as_view(),
        name="follow_list",
    ),
    path(
        "edit_profile/<int:pk>",
        views.ProfileEditView.as_view(),
        name="edit_profile",
    ),
    path("search/", views.SearchView.as_view(), name="search"),
    path("like/<int:pk>", views.PostLikeAPIView.as_view(), name="like"),
    path("comment/<int:post_pk>", views.CommentView.as_view(), name="comment")
]
