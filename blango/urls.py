"""
blango URL Configuration

The `urlpatterns` list routes URLs to views.
"""

import debug_toolbar

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django_registration.backends.activation.views import RegistrationView

import blog.views
import blango_auth.views
from blango_auth.forms import BlangoRegistrationForm


urlpatterns = [

    # Django admin
    path(
        "admin/",
        admin.site.urls,
    ),

    # Django login/logout/password management
    path(
        "accounts/",
        include("django.contrib.auth.urls"),
    ),

    # Registration page using custom User model
    path(
        "accounts/register/",
        RegistrationView.as_view(
            form_class=BlangoRegistrationForm,
        ),
        name="django_registration_register",
    ),

    # Two-step activation URLs
    path(
        "accounts/",
        include("django_registration.backends.activation.urls"),
    ),

    # User profile
    path(
        "accounts/profile/",
        blango_auth.views.profile,
        name="profile",
    ),

    # Blog homepage
    path(
        "",
        blog.views.index,
        name="index",
    ),

    # Blog grid
    path(
        "grid/",
        blog.views.grid,
        name="grid",
    ),

    # Blog post details
    path(
        "post/<slug:slug>/",
        blog.views.post_detail,
        name="post_detail",
    ),

    # Debug toolbar IP helper
    path(
        "ip/",
        blog.views.get_ip,
        name="get_ip",
    ),
]


# Enable Django Debug Toolbar only in development
if settings.DEBUG:
    urlpatterns += [
        path(
            "__debug__/",
            include(debug_toolbar.urls),
        ),
    ]


print(f"Time zone: {settings.TIME_ZONE}")