"""
blango URL Configuration

The `urlpatterns` list routes URLs to views.
"""

import debug_toolbar

from django.conf import settings
from django.contrib import admin
from django.urls import include, path

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

    # View used to determine the client's IP address
    path("ip/", blog.views.get_ip, name="get_ip"),
]

# Only enable Django Debug Toolbar in development
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

print(f"Time zone: {settings.TIME_ZONE}")