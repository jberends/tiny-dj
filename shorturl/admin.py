from django.contrib import admin

from shorturl.models import Hit
from shorturl.models import ShortUrl

# Register your models here.

admin.site.register(ShortUrl)
admin.site.register(Hit)
