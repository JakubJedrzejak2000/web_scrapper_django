import uuid

from django.db import models

class Web(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    article_name = models.TextField(null=True, blank=True)
    original_content = models.TextField(null=True, blank=True)
    text_content = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
