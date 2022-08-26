"""dgmenu URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

# debug setting for static files
from django.conf import settings
from django.conf.urls.static import static

from dgmenu_cafe.views import partial_view, header_partial_view, footer_partial_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dgmenu_cafe.urls', namespace='dgmenu_cafe')),
    path('', include('dgmenu_cafe_team.urls', namespace='dgmenu_cafe_team')),
    url(r'^partial-view/(?P<CafeUserId>\w+)$',
        partial_view,
        name='partial_view'),
    url(r'^header_partial-view/(?P<CafeUserId>\w+)$',
        header_partial_view,
        name='header_partial_view'),
    url(r'^footer_partial-view/(?P<CafeUserId>\w+)$',
        footer_partial_view,
        name='footer_partial_view'),
]
if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
