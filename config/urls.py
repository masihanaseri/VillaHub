from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import (
    SetActiveTownshipView,
    SignupView,
    CreateInvitationView,
    AcceptInviteView,
)

urlpatterns = [

    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "dashboard/",
        include("dashboard.urls"),
    ),

    path(
        "api/",
        include("api.urls"),
    ),

    path(
        "api/reservations/",
        include("reservations.urls"),
    ),

    # -----------------------------
    # Accounts
    # -----------------------------

    path(
        "auth/signup/",
        SignupView.as_view(),
        name="signup",
    ),

    path(
        "auth/set-township/",
        SetActiveTownshipView.as_view(),
        name="set-township",
    ),

    path(
        "auth/invite/create/",
        CreateInvitationView.as_view(),
        name="create-invitation",
    ),

    path(
        "auth/invite/<uuid:token>/accept/",
        AcceptInviteView.as_view(),
        name="accept-invite",
    ),

    path(
        "api/notifications/",
        include("notifications.urls"),
    ),

]

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )