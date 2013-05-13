# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pulsar.jname'
        db.add_column(u'database_pulsar', 'jname',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Pulsar.jname'
        db.delete_column(u'database_pulsar', 'jname')


    models = {
        u'database.pulsar': {
            'Meta': {'object_name': 'Pulsar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        }
    }

    complete_apps = ['database']