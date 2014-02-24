import uuid
from django.conf import settings
from django.db import models


class TemporaryUpload(models.Model):
    file = models.FileField(upload_to="temporary_upload")
    hash = models.CharField(max_length=32, editable=False, unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def ensure_hash(self):
        if not self.hash:
            self.hash = uuid.uuid4()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.ensure_hash()
        super(TemporaryUpload, self).save(force_insert, force_update, using, update_fields)

