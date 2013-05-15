# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Calculations.psr_id'
        db.alter_column(u'database_calculations', 'psr_id_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database.Pulsar'], null=True))

        # Changing field 'Geometry.psr_id'
        db.alter_column(u'database_geometry', 'psr_id_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database.Pulsar'], null=True))
        # Deleting field 'XrayFit.psr_id'
        db.delete_column(u'database_xrayfit', 'psr_id_id')

        # Adding field 'XrayFit.article_id'
        db.add_column(u'database_xrayfit', 'article_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['database.XrayArticle'], null=True),
                      keep_default=False)

        # Deleting field 'XrayComponent.xray_id'
        db.delete_column(u'database_xraycomponent', 'xray_id_id')

        # Adding field 'XrayComponent.fit_id'
        db.add_column(u'database_xraycomponent', 'fit_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['database.XrayFit'], null=True),
                      keep_default=False)


        # Changing field 'Subpulses.psr_id'
        db.alter_column(u'database_subpulses', 'psr_id_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database.Pulsar'], null=True))

        # Changing field 'Additional.psr_id'
        db.alter_column(u'database_additional', 'psr_id_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database.Pulsar'], null=True))

        # Changing field 'XrayArticle.psr_id'
        db.alter_column(u'database_xrayarticle', 'psr_id_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['database.Pulsar'], null=True))

    def backwards(self, orm):

        # Changing field 'Calculations.psr_id'
        db.alter_column(u'database_calculations', 'psr_id_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['database.Pulsar']))

        # Changing field 'Geometry.psr_id'
        db.alter_column(u'database_geometry', 'psr_id_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['database.Pulsar']))
        # Adding field 'XrayFit.psr_id'
        db.add_column(u'database_xrayfit', 'psr_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['database.XrayArticle']),
                      keep_default=False)

        # Deleting field 'XrayFit.article_id'
        db.delete_column(u'database_xrayfit', 'article_id_id')

        # Adding field 'XrayComponent.xray_id'
        db.add_column(u'database_xraycomponent', 'xray_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['database.XrayFit']),
                      keep_default=False)

        # Deleting field 'XrayComponent.fit_id'
        db.delete_column(u'database_xraycomponent', 'fit_id_id')


        # Changing field 'Subpulses.psr_id'
        db.alter_column(u'database_subpulses', 'psr_id_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['database.Pulsar']))

        # Changing field 'Additional.psr_id'
        db.alter_column(u'database_additional', 'psr_id_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['database.Pulsar']))

        # Changing field 'XrayArticle.psr_id'
        db.alter_column(u'database_xrayarticle', 'psr_id_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['database.Pulsar']))

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
            'psr_id': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['database.Pulsar']", 'null': 'True'})
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
            'psr_id': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['database.Pulsar']", 'null': 'True', 'blank': 'True'}),
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
            'psr_id': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['database.Pulsar']", 'null': 'True'}),
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
            'psr_id': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['database.Pulsar']", 'null': 'True'})
        },
        u'database.xrayarticle': {
            'Meta': {'object_name': 'XrayArticle'},
            'article': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'cite': ('django.db.models.fields.TextField', [], {'default': "'\\\\cite{}'"}),
            'dist': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'psr_id': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['database.Pulsar']", 'null': 'True'})
        },
        u'database.xraycomponent': {
            'Meta': {'object_name': 'XrayComponent'},
            'b_atm': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'fit_id': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['database.XrayFit']", 'null': 'True'}),
            'flux': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'flux_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'flux_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lum': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'lum_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'lum_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pl': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'pl_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'pl_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'r': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'r_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'r_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'spec_type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            't': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            't_minus': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            't_plus': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        },
        u'database.xrayfit': {
            'Meta': {'object_name': 'XrayFit'},
            'article_id': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['database.XrayArticle']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ordinal': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'spectrum': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        }
    }

    complete_apps = ['database']