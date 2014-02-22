from django.db import models


class TemporaryUpload(models.Model):
    file = models.FileField(upload_to="temporary_upload")