from django.contrib import admin
from oneblog.models import *

admin.autodiscover()
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
