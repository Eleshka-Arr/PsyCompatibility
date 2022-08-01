from django.contrib import admin
from ous.models import Ous
from ous.models import Author

admin.sites.site.register(Ous)
admin.sites.site.register(Author)
