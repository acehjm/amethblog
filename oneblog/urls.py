from django.conf.urls import url
from oneblog.views import *
from oneblog.views import RSSFeed


urlpatterns = [
    url(r'^$', article),
    url(r'^page/(?P<id>\d+)/$', detail, name='detail'),
    url(r'^archives/$', archives, name='archives'),
    url(r'^aboutme/$', aboutme, name='aboutme'),
    url(r'^tag/(?P<tag>\w+)/$', search_tag, name='search_tag'),
    url(r'^search/$',blog_search, name='search'),
    url(r'^feed/$', RSSFeed(), name = "RSS"),
]

urlpatterns += [
    url(r'^category/(?P<cg>\w+)$', post_list_by_category, name='list_by_cg'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',ArticleMonthArchiveView.as_view(month_format='%m'),name='archive_month_numeric'),
]