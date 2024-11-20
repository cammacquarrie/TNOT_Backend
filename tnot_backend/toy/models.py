import uuid

from django.conf import settings
from django.db import models

from useraccount.models import User



class Toy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    min_age_in_months = models.IntegerField()
    max_age_in_months = models.IntegerField()
    display_age = models.CharField(max_length=20)
    price = models.FloatField()
    amazon_link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/properties')
    created_at = models.DateTimeField(auto_now_add=True)

    def image_url(self):
        return f'{settings.WEBSITE_URL}{self.image.url}'