from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from champions.views import champions
from homepage.views import homepage
from items.views import items
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', homepage, name='homepage'),
    url(r'^champions/$', champions, name='champions'),
    url(r'^items/$', items, name='items'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
