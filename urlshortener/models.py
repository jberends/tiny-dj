import uuid

from django.db import models
# Create your models here.
from urlshortener.helpers import create_random_code


class ShortUrl(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    long_url = models.URLField()
    short_url = models.CharField(unique=True, max_length=64, blank=True, db_index=True)
    is_active = models.BooleanField(default=True)

    class Meta:

        ordering = ["-created_at"]

    def __str__(self):
        return f'{self.long_url} > {self.short_url}'


    @classmethod
    def create_shortened_url(cls):
        random_code = create_random_code()

        #check uniqueness
        if cls.objects.filter(short_url=random_code).exists():
            return cls.create_shortened_url()

        return random_code

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.create_shortened_url()

        super().save(*args, **kwargs)
