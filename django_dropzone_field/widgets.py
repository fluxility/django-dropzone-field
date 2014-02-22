from django.forms import HiddenInput
from django.utils.safestring import mark_safe


class DropzoneWidget(HiddenInput):
    def render(self, name, value, attrs=None):
        response = super(DropzoneWidget, self).render(name, value, attrs)
        response += "Dropzone construction site"

        return mark_safe(response)