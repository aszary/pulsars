# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Calculations'
        db.create_table(u'database_calculations', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('psr_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database.Pulsar'])),
            ('cos_i', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('f', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('dotP_15', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('bsurf2', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('b_14dp', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('l_sd', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('a_dp', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('r_dp', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('a', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('b', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('b_14', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('b_14_plus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('b_14_minus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'database', ['Calculations'])

        # Adding model 'Geometry'
        db.create_table(u'database_geometry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('psr_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database.Pulsar'])),
            ('article', self.gf('django.db.models.fields.TextField')(default='')),
            ('cite', self.gf('django.db.models.fields.TextField')(default='\\cite{}')),
            ('info', self.gf('django.db.models.fields.TextField')(default='')),
            ('alpha', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('beta', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('rho', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'database', ['Geometry'])

        # Adding model 'XrayFit'
        db.create_table(u'database_xrayfit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('psr_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database.XrayArticle'])),
            ('ordinal', self.gf('django.db.models.fields.IntegerField')(default=-1)),
            ('importance', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('spectrum', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal(u'database', ['XrayFit'])

        # Adding model 'XrayComponent'
        db.create_table(u'database_xraycomponent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('xray_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database.XrayFit'])),
            ('spec_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lum', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('lum_plus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('lum_minus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('flux', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('flux_plus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('flux_minus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('t', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('t_plus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('t_minus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('r', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('r_plus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('r_minus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('pl', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('pl_plus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('pl_minus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('b_atm', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'database', ['XrayComponent'])

        # Adding model 'Subpulses'
        db.create_table(u'database_subpulses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('psr_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database.Pulsar'])),
            ('article', self.gf('django.db.models.fields.TextField')(default='')),
            ('cite', self.gf('django.db.models.fields.TextField')(default='\\cite{}')),
            ('info', self.gf('django.db.models.fields.TextField')(default='')),
            ('p2', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('p2_plus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('p2_minus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('p3', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('p3_plus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('p3_minus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('p4', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'database', ['Subpulses'])

        # Adding model 'Additional'
        db.create_table(u'database_additional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('psr_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database.Pulsar'])),
            ('articles', self.gf('django.db.models.fields.TextField')(default='')),
            ('best_age', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('dist_dm_cl', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('dist_dm_cl_plus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('dist_dm_cl_minus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('dist_pi', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('dist_pi_plus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('dist_pi_minus', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal(u'database', ['Additional'])

        # Adding model 'XrayArticle'
        db.create_table(u'database_xrayarticle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('psr_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database.Pulsar'])),
            ('article', self.gf('django.db.models.fields.TextField')(default='')),
            ('cite', self.gf('django.db.models.fields.TextField')(default='\\cite{}')),
            ('info', self.gf('django.db.models.fields.TextField')(default='')),
            ('dist', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('importance', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'database', ['XrayArticle'])

        # Adding field 'Pulsar.comment'
        db.add_column(u'database_pulsar', 'comment',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Calculations'
        db.delete_table(u'database_calculations')

        # Deleting model 'Geometry'
        db.delete_table(u'database_geometry')

        # Deleting model 'XrayFit'
        db.delete_table(u'database_xrayfit')

        # Deleting model 'XrayComponent'
        db.delete_table(u'database_xraycomponent')

        # Deleting model 'Subpulses'
        db.delete_table(u'database_subpulses')

        # Deleting model 'Additional'
        db.delete_table(u'database_additional')

        # Deleting model 'XrayArticle'
        db.delete_table(u'database_xrayarticle')

        # Deleting field 'Pulsar.comment'
        db.delete_column(u'database_pulsar', 'comment')


    models = {
        u'database.additional': {
            'Meta': {'object_name': 'Additional'},
            'articles': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'best_age': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'dist_dm_cl': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'dist_dm_cl_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'dist_dm_cl_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'dist_pi': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'dist_pi_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'dist_pi_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'psr_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['database.Pulsar']"})
        },
        u'database.calculations': {
            'Meta': {'object_name': 'Calculations'},
            'a': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'a_dp': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'b': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'b_14': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'b_14_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'b_14_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'b_14dp': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'bsurf2': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'cos_i': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'dotP_15': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'f': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'l_sd': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'psr_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['database.Pulsar']"}),
            'r_dp': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        },
        u'database.geometry': {
            'Meta': {'object_name': 'Geometry'},
            'alpha': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'article': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'beta': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'cite': ('django.db.models.fields.TextField', [], {'default': "'\\\\cite{}'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'psr_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['database.Pulsar']"}),
            'rho': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
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
            'comment': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'simbad_link': ('django.db.models.fields.TextField', [], {'default': "'http://simbad.u-strasbg.fr'"}),
            'spindx': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'spindx_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        },
        u'database.subpulses': {
            'Meta': {'object_name': 'Subpulses'},
            'article': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'cite': ('django.db.models.fields.TextField', [], {'default': "'\\\\cite{}'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'p2': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'p2_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'p2_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'p3': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'p3_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'p3_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'p4': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'psr_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['database.Pulsar']"})
        },
        u'database.xrayarticle': {
            'Meta': {'object_name': 'XrayArticle'},
            'article': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'cite': ('django.db.models.fields.TextField', [], {'default': "'\\\\cite{}'"}),
            'dist': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'info': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'psr_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['database.Pulsar']"})
        },
        u'database.xraycomponent': {
            'Meta': {'object_name': 'XrayComponent'},
            'b_atm': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'flux': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'flux_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'flux_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lum': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'lum_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'lum_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'pl': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'pl_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'pl_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'r': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'r_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'r_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'spec_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            't': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            't_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            't_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'xray_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['database.XrayFit']"})
        },
        u'database.xrayfit': {
            'Meta': {'object_name': 'XrayFit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ordinal': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'psr_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['database.XrayArticle']"}),
            'spectrum': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        }
    }

    complete_apps = ['database']