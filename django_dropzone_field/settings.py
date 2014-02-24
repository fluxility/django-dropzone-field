from django.conf import settings

# Time after which an image should be removed in minutes
DROPZONE_FIELD_EXPIRATION_TIME = getattr(settings, 'DROPZONE_FIELD_EXPIRATION_TIME', 15)