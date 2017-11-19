from django.conf.urls import url
from django.conf import settings
from django.contrib import admin

admin.site.site_header = settings.HEADER

urlpatterns = [
    url(r'^', admin.site.urls),
]
