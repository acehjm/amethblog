#coding=utf-8
from django.conf.urls import include, url
from material.frontend import urls as frontend_urls
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'', include('oneblog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(frontend_urls)),
]