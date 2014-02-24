from django.contrib import admin
from django.db.models import FileField
from django_dropzone_field.fields import DropzoneField

from .models import SomeModel


class SomeModelAdmin(admin.ModelAdmin):
    model = SomeModel

    formfield_overrides = {
        FileField: {'form_class': DropzoneField}
    }


admin.site.register(SomeModel, SomeModelAdmin)