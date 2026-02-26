from django.contrib import admin
from django.urls import path, include
from studentorg.views import HomePageView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Login/Logout URLs (Django built-in)
    path("accounts/", include("django.contrib.auth.urls")),

    path("", HomePageView.as_view(), name="home"),
    path("", include("studentorg.urls")),
]