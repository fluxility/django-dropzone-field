from django.template.defaultfilters import register
from django.utils.safestring import mark_safe
from easy_thumbnails.exceptions import InvalidImageFormatError
from easy_thumbnails.files import get_thumbnailer


@register.filter
def file_reference(value, width=100, height=100):
    """
    Returns an thumbnail image if possible (is readable image). Otherwise
    return a link to the file.

    :param value:   File object
    :param width:   Width of thumbnail
    :param height:  Height of thumbnail
    :return:
    """
    try:
        options = {
            'size': (width, height),
            'crop': True
        }
        url = get_thumbnailer(value).get_thumbnail(options).url

        value = """<img src="%s">""" % url
    except InvalidImageFormatError:
        value = """<a href="%s">%s</a>""" % (value.url, value.url)

    return mark_safe(value)