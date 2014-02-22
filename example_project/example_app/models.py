from django.db import models


class SomeModel(models.Model):
    some_file_field = models.FileField(upload_to="some_folder")