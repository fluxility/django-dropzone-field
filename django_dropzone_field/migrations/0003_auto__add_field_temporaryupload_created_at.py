# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TemporaryUpload.created_at'
        db.add_column(u'django_dropzone_field_temporaryupload', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 2, 24, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TemporaryUpload.created_at'
        db.delete_column(u'django_dropzone_field_temporaryupload', 'created_at')


    models = {
        u'django_dropzone_field.temporaryupload': {
            'Meta': {'object_name': 'TemporaryUpload'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'hash': ('django.db.models.fields.CharField', [], {'max_length': '32', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['django_dropzone_field']