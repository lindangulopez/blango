"""
blango URL Configuration

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings

import blog.views


urlpatterns = [
    path("admin/", admin.site.urls),

    path("accounts/", include("django.contrib.auth.urls")),

    path("", blog.views.index, name="index"),

    path("grid/", blog.views.grid, name="grid"),

    path(
        "post/<slug:slug>/",
        blog.views.post_detail,
        name="post_detail",
    ),
]


print(f"Time zone: {settings.TIME_ZONE}")