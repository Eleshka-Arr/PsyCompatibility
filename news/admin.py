from django.contrib import admin
from news.models import Articles

admin.sites.site.register(Articles)
