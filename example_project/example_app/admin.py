from django.contrib import admin
from django.db.models import FileField

from django_dropzone_field.widgets import DropzoneWidget
from .models import SomeModel


class SomeModelAdmin(admin.ModelAdmin):
    model = SomeModel

    formfield_overrides = {
        FileField: {'widget': DropzoneWidget}
    }


admin.site.register(SomeModel, SomeModelAdmin)