# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pulsar'
        db.create_table(u'database_pulsar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'database', ['Pulsar'])


    def backwards(self, orm):
        # Deleting model 'Pulsar'
        db.delete_table(u'database_pulsar')


    models = {
        u'database.pulsar': {
            'Meta': {'object_name': 'Pulsar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['database']