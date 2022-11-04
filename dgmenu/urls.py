from django.contrib import sitemaps
from django.urls import reverse
from dgmenu_cafe.models import Cafe

all_cafe = Cafe.objects.filter(Admin_Is_Active=True).all()
cafe = []
for i in all_cafe:
    cafe.append(i.Cafe_UserName)


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['dgmenu_site_home:site_home_page']

    def location(self, item):
        return reverse(item)


class MenuViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return cafe

    def location(self, item):
        return reverse('dgmenu_cafe:cafe_home', kwargs={'cafename': 'demo'})


from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import handler404, handler500
# debug setting for static files
from django.conf import settings
from django.conf.urls.static import static

from dgmenu_cafe.views import partial_view, header_partial_view, footer_partial_view
from adminpanel.views import header_references_partial_view, header_panel_partial_view, quick_bar_panel_partial_view, \
    navbar_panel_partial_view
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap,
    'menu': MenuViewSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminpanel/', include('adminpanel.urls', namespace='adminpanel')),
    path('adminpanel/category/', include('adminpanel_category.urls', namespace='adminpanel_category')),
    path('adminpanel/food/', include('adminpanel_food.urls', namespace='adminpanel_food')),
    path('adminpanel/gallery/', include('adminpanel_gallery.urls', namespace='adminpanel_gallery')),
    path('adminpanel/team/', include('adminpanel_team.urls', namespace='adminpanel_team')),
    path('adminpanel/about/', include('adminpanel_about.urls', namespace='adminpanel_about')),
    path('adminpanel/settings/', include('adminpanel_cafe_settings.urls', namespace='adminpanel_settings')),
    path('', include('dgmenu_site_home.urls', namespace='dgmenu_site_home')),
    path('', include('dgmenu_cafe.urls', namespace='dgmenu_cafe')),
    path('', include('dgmenu_cafe_team.urls', namespace='dgmenu_cafe_team')),
    path('', include('dgmenu_cafe_about.urls', namespace='dgmenu_cafe_about')),
    path('', include('dgmenu_cafe_gallery.urls', namespace='dgmenu_cafe_gallery')),
    path('accounts/', include('dgmenu_account.urls', namespace='dgmenu_cafe_account')),
    url(r'^partial-view/(?P<CafeUserId>\w+)$',
        partial_view,
        name='partial_view'),
    url(r'^header_partial-view/(?P<CafeUserId>\w+)$',
        header_partial_view,
        name='header_partial_view'),
    url(r'^footer_partial-view/(?P<CafeUserId>\w+)$',
        footer_partial_view,
        name='footer_partial_view'),
    # admin header_references_partial_view
    url(r'^header_references_partial_view',
        header_references_partial_view,
        name='header_references_partial_view'),
    url(r'^header_panel_partial_view',
        header_panel_partial_view,
        name='header_panel_partial_view'),
    url(r'^quick_bar_panel_partial_view',
        quick_bar_panel_partial_view,
        name='quick_bar_panel_partial_view'),
    url(r'^navbar_panel_partial_view',
        navbar_panel_partial_view,
        name='navbar_panel_partial_view'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

]
handler404 = handler404
handler500 = handler500

# add root static files
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# add media static files
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
