# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TemporaryUpload'
        db.create_table(u'django_dropzone_field_temporaryupload', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'django_dropzone_field', ['TemporaryUpload'])


    def backwards(self, orm):
        # Deleting model 'TemporaryUpload'
        db.delete_table(u'django_dropzone_field_temporaryupload')


    models = {
        u'django_dropzone_field.temporaryupload': {
            'Meta': {'object_name': 'TemporaryUpload'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['django_dropzone_field']