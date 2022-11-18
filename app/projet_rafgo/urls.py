"""projet_rafgo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static

# Core Django imports for auth
from django.contrib.auth import views as auth_views


urlpatterns=i18n_patterns(
    path('', include('website.urls')),
    path(_('admin/'), admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', include('blog.urls', namespace='blog')), # Urls for blog app.
    path('api/v1/', include('blog.api.v1.routers.routers')), 
    # re_path(r'^rosetta/', include('rosetta.urls'))

    ########## - urls for accounts 
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/v1/article/', include('blog.api.v1.routers.routers')), # Urls for API.

    # Url for password reset.
    path('account/password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='account/password_reset.html'),
         name='password_reset'),

    # Url for successful password reset.
    path('account/password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='account/password_reset_done.html'),
         name='password_reset_done'),

    # Url for successful password reset confirm.
    path('account/password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='account/password_reset_confirm.html'),
         name='password_reset_confirm'),

    # Url for password reset done.
    path('account/password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),

    ##########

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

    import debug_toolbar
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns


# Modifies default django admin titles and headers with custom app detail.
admin.site.site_header = "RAFGO Admin"
admin.site.site_title = "RAFGO Admin Portal"
admin.site.index_title = "Welcome to RAFGO Platform Portal"