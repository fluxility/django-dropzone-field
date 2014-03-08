from django.db import models


class SomeModel(models.Model):
    some_char_field = models.CharField(max_length=100, null=True)
    some_file_field = models.FileField(upload_to="some_folder")
    a_second_file_field = models.FileField(upload_to="some_folder")