"""blango URL Configuration

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include

import blog.views


urlpatterns = [
    path("admin/", admin.site.urls),

    # Django built-in authentication URLs
    path("accounts/", include("django.contrib.auth.urls")),

    # Blog homepage
    path("", blog.views.index, name="index"),

    # Blog grid page
    path("grid/", blog.views.grid, name="grid"),

    # Individual post page with comments
    path(
        "post/<slug:slug>/",
        blog.views.post_detail,
        name="post_detail",
    ),
]