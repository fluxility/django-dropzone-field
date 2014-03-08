from django.core import validators
from django.core.exceptions import ValidationError
from django.core.files import File
from django.forms.fields import Field, FileField
from django_dropzone_field.models import TemporaryUpload
from django_dropzone_field.widgets import DropzoneWidget


class DropzoneField(FileField):
    widget = DropzoneWidget

    def __init__(self, *args, **kwargs):
        if not hasattr(self, 'empty_values'):
            self.empty_values = list(validators.EMPTY_VALUES)

        super(DropzoneField, self).__init__(*args, **kwargs)


    def bound_data(self, data, initial):
        if data in self.empty_values:
            return initial

        return initial, self.get_temporary_upload(data)

    @staticmethod
    def get_temporary_upload(value):
        try:
            return TemporaryUpload.objects.get(hash=value)
        except TemporaryUpload.DoesNotExist:
            raise ValidationError("Selected image does not exist")

        return None

    def clean(self, data, initial=None):
        return super(DropzoneField, self).clean(data, initial)

    def to_python(self, value):
        if value in self.empty_values:
            return None

        upload = self.get_temporary_upload(value)
        file_object = File(upload.file)
        return file_object










