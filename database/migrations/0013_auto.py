# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field subpulse on 'Pulsar'
        db.delete_table('database_pulsar_subpulse')

        # Removing M2M table for field geometry on 'Pulsar'
        db.delete_table('database_pulsar_geometry')

        # Removing M2M table for field additional on 'Pulsar'
        db.delete_table('database_pulsar_additional')

        # Removing M2M table for field calculation on 'Pulsar'
        db.delete_table('database_pulsar_calculation')

        # Adding M2M table for field geometries on 'Pulsar'
        db.create_table(u'database_pulsar_geometries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pulsar', models.ForeignKey(orm[u'database.pulsar'], null=False)),
            ('geometry', models.ForeignKey(orm[u'database.geometry'], null=False))
        ))
        db.create_unique(u'database_pulsar_geometries', ['pulsar_id', 'geometry_id'])

        # Adding M2M table for field subpulses on 'Pulsar'
        db.create_table(u'database_pulsar_subpulses', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pulsar', models.ForeignKey(orm[u'database.pulsar'], null=False)),
            ('subpulse', models.ForeignKey(orm[u'database.subpulse'], null=False))
        ))
        db.create_unique(u'database_pulsar_subpulses', ['pulsar_id', 'subpulse_id'])

        # Adding M2M table for field additionals on 'Pulsar'
        db.create_table(u'database_pulsar_additionals', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pulsar', models.ForeignKey(orm[u'database.pulsar'], null=False)),
            ('additional', models.ForeignKey(orm[u'database.additional'], null=False))
        ))
        db.create_unique(u'database_pulsar_additionals', ['pulsar_id', 'additional_id'])

        # Adding M2M table for field calculations on 'Pulsar'
        db.create_table(u'database_pulsar_calculations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pulsar', models.ForeignKey(orm[u'database.pulsar'], null=False)),
            ('calculation', models.ForeignKey(orm[u'database.calculation'], null=False))
        ))
        db.create_unique(u'database_pulsar_calculations', ['pulsar_id', 'calculation_id'])


    def backwards(self, orm):
        # Adding M2M table for field subpulse on 'Pulsar'
        db.create_table(u'database_pulsar_subpulse', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pulsar', models.ForeignKey(orm[u'database.pulsar'], null=False)),
            ('subpulse', models.ForeignKey(orm[u'database.subpulse'], null=False))
        ))
        db.create_unique(u'database_pulsar_subpulse', ['pulsar_id', 'subpulse_id'])

        # Adding M2M table for field geometry on 'Pulsar'
        db.create_table(u'database_pulsar_geometry', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pulsar', models.ForeignKey(orm[u'database.pulsar'], null=False)),
            ('geometry', models.ForeignKey(orm[u'database.geometry'], null=False))
        ))
        db.create_unique(u'database_pulsar_geometry', ['pulsar_id', 'geometry_id'])

        # Adding M2M table for field additional on 'Pulsar'
        db.create_table(u'database_pulsar_additional', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pulsar', models.ForeignKey(orm[u'database.pulsar'], null=False)),
            ('additional', models.ForeignKey(orm[u'database.additional'], null=False))
        ))
        db.create_unique(u'database_pulsar_additional', ['pulsar_id', 'additional_id'])

        # Adding M2M table for field calculation on 'Pulsar'
        db.create_table(u'database_pulsar_calculation', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pulsar', models.ForeignKey(orm[u'database.pulsar'], null=False)),
            ('calculation', models.ForeignKey(orm[u'database.calculation'], null=False))
        ))
        db.create_unique(u'database_pulsar_calculation', ['pulsar_id', 'calculation_id'])

        # Removing M2M table for field geometries on 'Pulsar'
        db.delete_table('database_pulsar_geometries')

        # Removing M2M table for field subpulses on 'Pulsar'
        db.delete_table('database_pulsar_subpulses')

        # Removing M2M table for field additionals on 'Pulsar'
        db.delete_table('database_pulsar_additionals')

        # Removing M2M table for field calculations on 'Pulsar'
        db.delete_table('database_pulsar_calculations')


    models = {
        u'database.additional': {
            'Meta': {'object_name': 'Additional'},
            'articles': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'best_age': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dist_dm_cl': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dist_dm_cl_minus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dist_dm_cl_plus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dist_pi': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dist_pi_minus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dist_pi_plus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'database.calculation': {
            'Meta': {'object_name': 'Calculation'},
            'a': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'a_dp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'b': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'b_14': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'b_14_minus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'b_14_plus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'b_14dp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bsurf2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cos_i': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'dotP_15': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'f': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'l_sd': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'r_dp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'database.geometry': {
            'Meta': {'object_name': 'Geometry'},
            'alpha': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'article': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'beta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cite': ('django.db.models.fields.TextField', [], {'default': "'\\\\cite{}'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rho': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'database.pulsar': {
            'A1': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'A1_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Age': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Age_i': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Assoc': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '255'}),
            'BSurf': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'BSurf_i': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'B_LC': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'BinComp': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'Binary': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'DM': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'DM1': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'DM1_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'DM_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'DMsinb': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Date': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'DecJ': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'DecJD': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'DecJ_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Dist': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Dist_DM': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ECC': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ECC_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ELat': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ELat_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ELong': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ELong_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Edot': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Edot_i': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Edotd2': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Eps1': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Eps1_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Eps2': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Eps2_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'F0': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'F0_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'F1': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'F1_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'F2': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'F2_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'F3': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'F3_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'GB': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'GL': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'JName': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'MedMass': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Meta': {'object_name': 'Pulsar'},
            'MinMass': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'NGlt': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Name': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'OM': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'OM_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'OSurvey': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '200'}),
            'P0': ('django.db.models.fields.DecimalField', [], {'default': "'-0.0'", 'max_digits': '22', 'decimal_places': '20'}),
            'P0_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'P1': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'P1_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'P1_i': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PB': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PB_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PEpoch': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PMDec': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PMDec_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PMElat': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PMElat_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PMElong': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PMElong_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PMRA': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PMRA_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PMTot': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PX': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PX_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'PosEpoch': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'RM': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'RM_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'R_Lum': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'R_Lum14': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'RaJ': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'RaJD': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'RaJ_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'S1400': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'S1400_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'S2000': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'S2000_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'S400': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'S400_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Survey': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '200'}),
            'T0': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'T0_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'TASC': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'TASC_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Tau_sc': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Tau_sc_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Type': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '200'}),
            'Units': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'VTrans': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'W10': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'W10_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'W50': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'W50_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'XX': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'YY': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ZZ': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'additionals': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.Additional']", 'symmetrical': 'False'}),
            'calculations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.Calculation']", 'symmetrical': 'False'}),
            'comment': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'geometries': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.Geometry']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'simbad_link': ('django.db.models.fields.TextField', [], {'default': "'http://simbad.u-strasbg.fr'"}),
            'spindx': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'spindx_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'subpulses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.Subpulse']", 'symmetrical': 'False'}),
            'xray_articles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.XrayArticle']", 'symmetrical': 'False'})
        },
        u'database.subpulse': {
            'Meta': {'object_name': 'Subpulse'},
            'article': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'cite': ('django.db.models.fields.TextField', [], {'default': "'\\\\cite{}'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'p2': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'p2_minus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'p2_plus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'p3': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'p3_minus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'p3_plus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'p4': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'database.xrayarticle': {
            'Meta': {'object_name': 'XrayArticle'},
            'article': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'cite': ('django.db.models.fields.TextField', [], {'default': "'\\\\cite{}'"}),
            'dist': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fits': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.XrayFit']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'database.xraycomponent': {
            'Meta': {'object_name': 'XrayComponent'},
            'b_atm': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'flux': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'flux_minus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'flux_plus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lum': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lum_minus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lum_plus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pl': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pl_minus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pl_plus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'r': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'r_minus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'r_plus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'spec_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            't': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            't_minus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            't_plus': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'database.xrayfit': {
            'Meta': {'object_name': 'XrayFit'},
            'components': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.XrayComponent']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ordinal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'spectrum': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        }
    }

    complete_apps = ['database']