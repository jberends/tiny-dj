from django.contrib import admin

# Register your models here.
from urlshortener.models import ShortUrl

admin.site.register(ShortUrl)
