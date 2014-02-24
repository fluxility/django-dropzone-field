from django.core.exceptions import ValidationError
from django.core.files import File
from django.forms.fields import Field, FileField
from django_dropzone_field.models import TemporaryUpload
from django_dropzone_field.widgets import DropzoneWidget


class DropzoneField(FileField):
    widget = DropzoneWidget

    def clean(self, data, initial=None):
        return super(DropzoneField, self).clean(data, initial)

    def to_python(self, value):
        try:
            upload = TemporaryUpload.objects.get(hash=value)
            file_object = File(upload.file)
            return file_object
        except TemporaryUpload.DoesNotExist:
            raise ValidationError("Selected image does not exist")







