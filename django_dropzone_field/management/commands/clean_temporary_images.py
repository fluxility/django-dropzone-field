from datetime import datetime, timedelta
from django.utils import timezone
from django.core.management import BaseCommand
from django_dropzone_field.models import TemporaryUpload
from ...settings import DROPZONE_FIELD_EXPIRATION_TIME


class Command(BaseCommand):
    help = 'Removes all TemporaryUploads that are older than settings.DROPZONE_FIELD_EXPIRATION_TIME minutes'

    def handle(self, *args, **options):
        expiration_datetime = timezone.now() - timedelta(minutes=DROPZONE_FIELD_EXPIRATION_TIME)
        TemporaryUpload.objects.filter(created_at__lte=expiration_datetime).delete()
