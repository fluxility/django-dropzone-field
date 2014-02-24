from django.forms import HiddenInput
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

DROPZONEJS_VERSION = '3.8.2'


class DropzoneWidget(HiddenInput):
    def render(self, name, value, attrs=None):
        response = super(DropzoneWidget, self).render(name, "", attrs)
        response += render_to_string('django_dropzone_field/widgets/dropzone.html')

        return mark_safe(response)

    class Media:
        js = (
            'js/django_dropzone_field/base.js',
            '//cdnjs.cloudflare.com/ajax/libs/dropzone/%s/dropzone.min.js' % DROPZONEJS_VERSION,
        )

        css = {
            'all': [
                '//cdnjs.cloudflare.com/ajax/libs/dropzone/%s/css/basic.css' % DROPZONEJS_VERSION,
                'css/django_dropzone_field/base.css',
            ]
        }