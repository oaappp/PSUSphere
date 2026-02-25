from django.contrib import admin
from django.urls import path, include
from studentorg.views import HomePageView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomePageView.as_view(), name="home"),
    path("", include("studentorg.urls")),
]