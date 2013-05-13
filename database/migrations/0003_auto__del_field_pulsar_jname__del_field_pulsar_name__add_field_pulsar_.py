# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Pulsar.jname'
        db.delete_column(u'database_pulsar', 'jname')

        # Deleting field 'Pulsar.name'
        db.delete_column(u'database_pulsar', 'name')

        # Adding field 'Pulsar.Name'
        db.add_column(u'database_pulsar', 'Name',
                      self.gf('django.db.models.fields.CharField')(default='None', max_length=200),
                      keep_default=False)

        # Adding field 'Pulsar.JName'
        db.add_column(u'database_pulsar', 'JName',
                      self.gf('django.db.models.fields.CharField')(default='None', max_length=200),
                      keep_default=False)

        # Adding field 'Pulsar.RaJ'
        db.add_column(u'database_pulsar', 'RaJ',
                      self.gf('django.db.models.fields.CharField')(default='None', max_length=200),
                      keep_default=False)

        # Adding field 'Pulsar.RaJ_err'
        db.add_column(u'database_pulsar', 'RaJ_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.DecJ'
        db.add_column(u'database_pulsar', 'DecJ',
                      self.gf('django.db.models.fields.CharField')(default='None', max_length=200),
                      keep_default=False)

        # Adding field 'Pulsar.DecJ_err'
        db.add_column(u'database_pulsar', 'DecJ_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PMRA'
        db.add_column(u'database_pulsar', 'PMRA',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PMRA_err'
        db.add_column(u'database_pulsar', 'PMRA_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PMDec'
        db.add_column(u'database_pulsar', 'PMDec',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PMDec_err'
        db.add_column(u'database_pulsar', 'PMDec_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PX'
        db.add_column(u'database_pulsar', 'PX',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PX_err'
        db.add_column(u'database_pulsar', 'PX_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PosEpoch'
        db.add_column(u'database_pulsar', 'PosEpoch',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.ELong'
        db.add_column(u'database_pulsar', 'ELong',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.ELong_err'
        db.add_column(u'database_pulsar', 'ELong_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.ELat'
        db.add_column(u'database_pulsar', 'ELat',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.ELat_err'
        db.add_column(u'database_pulsar', 'ELat_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PMElong'
        db.add_column(u'database_pulsar', 'PMElong',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PMElong_err'
        db.add_column(u'database_pulsar', 'PMElong_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PMElat'
        db.add_column(u'database_pulsar', 'PMElat',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PMElat_err'
        db.add_column(u'database_pulsar', 'PMElat_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.GL'
        db.add_column(u'database_pulsar', 'GL',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.GB'
        db.add_column(u'database_pulsar', 'GB',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.RAJD'
        db.add_column(u'database_pulsar', 'RAJD',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.DecJD'
        db.add_column(u'database_pulsar', 'DecJD',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.P0'
        db.add_column(u'database_pulsar', 'P0',
                      self.gf('django.db.models.fields.DecimalField')(default='-0.0', max_digits=22, decimal_places=20),
                      keep_default=False)

        # Adding field 'Pulsar.P0_err'
        db.add_column(u'database_pulsar', 'P0_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.P1'
        db.add_column(u'database_pulsar', 'P1',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.P1_err'
        db.add_column(u'database_pulsar', 'P1_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.F0'
        db.add_column(u'database_pulsar', 'F0',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.F0_err'
        db.add_column(u'database_pulsar', 'F0_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.F1'
        db.add_column(u'database_pulsar', 'F1',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.F1_err'
        db.add_column(u'database_pulsar', 'F1_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.F2'
        db.add_column(u'database_pulsar', 'F2',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.F2_err'
        db.add_column(u'database_pulsar', 'F2_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.F3'
        db.add_column(u'database_pulsar', 'F3',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.F3_err'
        db.add_column(u'database_pulsar', 'F3_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PEpoch'
        db.add_column(u'database_pulsar', 'PEpoch',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.DM'
        db.add_column(u'database_pulsar', 'DM',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.DM_err'
        db.add_column(u'database_pulsar', 'DM_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.DM1'
        db.add_column(u'database_pulsar', 'DM1',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.DM1_err'
        db.add_column(u'database_pulsar', 'DM1_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.RM'
        db.add_column(u'database_pulsar', 'RM',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.RM_err'
        db.add_column(u'database_pulsar', 'RM_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.W50'
        db.add_column(u'database_pulsar', 'W50',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.W50_err'
        db.add_column(u'database_pulsar', 'W50_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.W10'
        db.add_column(u'database_pulsar', 'W10',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.W10_err'
        db.add_column(u'database_pulsar', 'W10_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Tau_sc'
        db.add_column(u'database_pulsar', 'Tau_sc',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Tau_sc_err'
        db.add_column(u'database_pulsar', 'Tau_sc_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.S400'
        db.add_column(u'database_pulsar', 'S400',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.S400_err'
        db.add_column(u'database_pulsar', 'S400_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.S1400'
        db.add_column(u'database_pulsar', 'S1400',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.S1400_err'
        db.add_column(u'database_pulsar', 'S1400_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.S2000'
        db.add_column(u'database_pulsar', 'S2000',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.S2000_err'
        db.add_column(u'database_pulsar', 'S2000_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.spindx'
        db.add_column(u'database_pulsar', 'spindx',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.spindx_err'
        db.add_column(u'database_pulsar', 'spindx_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Binary'
        db.add_column(u'database_pulsar', 'Binary',
                      self.gf('django.db.models.fields.CharField')(default='*', max_length=200),
                      keep_default=False)

        # Adding field 'Pulsar.T0'
        db.add_column(u'database_pulsar', 'T0',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.T0_err'
        db.add_column(u'database_pulsar', 'T0_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PB'
        db.add_column(u'database_pulsar', 'PB',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PB_err'
        db.add_column(u'database_pulsar', 'PB_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.A1'
        db.add_column(u'database_pulsar', 'A1',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.A1_err'
        db.add_column(u'database_pulsar', 'A1_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.OM'
        db.add_column(u'database_pulsar', 'OM',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.OM_err'
        db.add_column(u'database_pulsar', 'OM_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.ECC'
        db.add_column(u'database_pulsar', 'ECC',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Ecc_err'
        db.add_column(u'database_pulsar', 'Ecc_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.TASC'
        db.add_column(u'database_pulsar', 'TASC',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.TASC_err'
        db.add_column(u'database_pulsar', 'TASC_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Eps1'
        db.add_column(u'database_pulsar', 'Eps1',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Eps1_err'
        db.add_column(u'database_pulsar', 'Eps1_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Eps2'
        db.add_column(u'database_pulsar', 'Eps2',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Eps2_err'
        db.add_column(u'database_pulsar', 'Eps2_err',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.MinMass'
        db.add_column(u'database_pulsar', 'MinMass',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.MedMass'
        db.add_column(u'database_pulsar', 'MedMass',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.BinComp'
        db.add_column(u'database_pulsar', 'BinComp',
                      self.gf('django.db.models.fields.CharField')(default='None', max_length=200),
                      keep_default=False)

        # Adding field 'Pulsar.Dist'
        db.add_column(u'database_pulsar', 'Dist',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Dist_DM'
        db.add_column(u'database_pulsar', 'Dist_DM',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.DMsinb'
        db.add_column(u'database_pulsar', 'DMsinb',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.ZZ'
        db.add_column(u'database_pulsar', 'ZZ',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.XX'
        db.add_column(u'database_pulsar', 'XX',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.YY'
        db.add_column(u'database_pulsar', 'YY',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Assoc'
        db.add_column(u'database_pulsar', 'Assoc',
                      self.gf('django.db.models.fields.CharField')(default='0', max_length=255),
                      keep_default=False)

        # Adding field 'Pulsar.Survey'
        db.add_column(u'database_pulsar', 'Survey',
                      self.gf('django.db.models.fields.CharField')(default='0', max_length=200),
                      keep_default=False)

        # Adding field 'Pulsar.OSurvey'
        db.add_column(u'database_pulsar', 'OSurvey',
                      self.gf('django.db.models.fields.CharField')(default='0', max_length=200),
                      keep_default=False)

        # Adding field 'Pulsar.Date'
        db.add_column(u'database_pulsar', 'Date',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Type'
        db.add_column(u'database_pulsar', 'Type',
                      self.gf('django.db.models.fields.CharField')(default='0', max_length=200),
                      keep_default=False)

        # Adding field 'Pulsar.NGlt'
        db.add_column(u'database_pulsar', 'NGlt',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Pulsar.R_Lum'
        db.add_column(u'database_pulsar', 'R_Lum',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.R_Lum14'
        db.add_column(u'database_pulsar', 'R_Lum14',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Age'
        db.add_column(u'database_pulsar', 'Age',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.BSurf'
        db.add_column(u'database_pulsar', 'BSurf',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Edot'
        db.add_column(u'database_pulsar', 'Edot',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Edotd2'
        db.add_column(u'database_pulsar', 'Edotd2',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.PMTot'
        db.add_column(u'database_pulsar', 'PMTot',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.VTrans'
        db.add_column(u'database_pulsar', 'VTrans',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.P1_i'
        db.add_column(u'database_pulsar', 'P1_i',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Age_i'
        db.add_column(u'database_pulsar', 'Age_i',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.BSurf_i'
        db.add_column(u'database_pulsar', 'BSurf_i',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.Edot_i'
        db.add_column(u'database_pulsar', 'Edot_i',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pulsar.B_LC'
        db.add_column(u'database_pulsar', 'B_LC',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Pulsar.jname'
        db.add_column(u'database_pulsar', 'jname',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Pulsar.name'
        db.add_column(u'database_pulsar', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Deleting field 'Pulsar.Name'
        db.delete_column(u'database_pulsar', 'Name')

        # Deleting field 'Pulsar.JName'
        db.delete_column(u'database_pulsar', 'JName')

        # Deleting field 'Pulsar.RaJ'
        db.delete_column(u'database_pulsar', 'RaJ')

        # Deleting field 'Pulsar.RaJ_err'
        db.delete_column(u'database_pulsar', 'RaJ_err')

        # Deleting field 'Pulsar.DecJ'
        db.delete_column(u'database_pulsar', 'DecJ')

        # Deleting field 'Pulsar.DecJ_err'
        db.delete_column(u'database_pulsar', 'DecJ_err')

        # Deleting field 'Pulsar.PMRA'
        db.delete_column(u'database_pulsar', 'PMRA')

        # Deleting field 'Pulsar.PMRA_err'
        db.delete_column(u'database_pulsar', 'PMRA_err')

        # Deleting field 'Pulsar.PMDec'
        db.delete_column(u'database_pulsar', 'PMDec')

        # Deleting field 'Pulsar.PMDec_err'
        db.delete_column(u'database_pulsar', 'PMDec_err')

        # Deleting field 'Pulsar.PX'
        db.delete_column(u'database_pulsar', 'PX')

        # Deleting field 'Pulsar.PX_err'
        db.delete_column(u'database_pulsar', 'PX_err')

        # Deleting field 'Pulsar.PosEpoch'
        db.delete_column(u'database_pulsar', 'PosEpoch')

        # Deleting field 'Pulsar.ELong'
        db.delete_column(u'database_pulsar', 'ELong')

        # Deleting field 'Pulsar.ELong_err'
        db.delete_column(u'database_pulsar', 'ELong_err')

        # Deleting field 'Pulsar.ELat'
        db.delete_column(u'database_pulsar', 'ELat')

        # Deleting field 'Pulsar.ELat_err'
        db.delete_column(u'database_pulsar', 'ELat_err')

        # Deleting field 'Pulsar.PMElong'
        db.delete_column(u'database_pulsar', 'PMElong')

        # Deleting field 'Pulsar.PMElong_err'
        db.delete_column(u'database_pulsar', 'PMElong_err')

        # Deleting field 'Pulsar.PMElat'
        db.delete_column(u'database_pulsar', 'PMElat')

        # Deleting field 'Pulsar.PMElat_err'
        db.delete_column(u'database_pulsar', 'PMElat_err')

        # Deleting field 'Pulsar.GL'
        db.delete_column(u'database_pulsar', 'GL')

        # Deleting field 'Pulsar.GB'
        db.delete_column(u'database_pulsar', 'GB')

        # Deleting field 'Pulsar.RAJD'
        db.delete_column(u'database_pulsar', 'RAJD')

        # Deleting field 'Pulsar.DecJD'
        db.delete_column(u'database_pulsar', 'DecJD')

        # Deleting field 'Pulsar.P0'
        db.delete_column(u'database_pulsar', 'P0')

        # Deleting field 'Pulsar.P0_err'
        db.delete_column(u'database_pulsar', 'P0_err')

        # Deleting field 'Pulsar.P1'
        db.delete_column(u'database_pulsar', 'P1')

        # Deleting field 'Pulsar.P1_err'
        db.delete_column(u'database_pulsar', 'P1_err')

        # Deleting field 'Pulsar.F0'
        db.delete_column(u'database_pulsar', 'F0')

        # Deleting field 'Pulsar.F0_err'
        db.delete_column(u'database_pulsar', 'F0_err')

        # Deleting field 'Pulsar.F1'
        db.delete_column(u'database_pulsar', 'F1')

        # Deleting field 'Pulsar.F1_err'
        db.delete_column(u'database_pulsar', 'F1_err')

        # Deleting field 'Pulsar.F2'
        db.delete_column(u'database_pulsar', 'F2')

        # Deleting field 'Pulsar.F2_err'
        db.delete_column(u'database_pulsar', 'F2_err')

        # Deleting field 'Pulsar.F3'
        db.delete_column(u'database_pulsar', 'F3')

        # Deleting field 'Pulsar.F3_err'
        db.delete_column(u'database_pulsar', 'F3_err')

        # Deleting field 'Pulsar.PEpoch'
        db.delete_column(u'database_pulsar', 'PEpoch')

        # Deleting field 'Pulsar.DM'
        db.delete_column(u'database_pulsar', 'DM')

        # Deleting field 'Pulsar.DM_err'
        db.delete_column(u'database_pulsar', 'DM_err')

        # Deleting field 'Pulsar.DM1'
        db.delete_column(u'database_pulsar', 'DM1')

        # Deleting field 'Pulsar.DM1_err'
        db.delete_column(u'database_pulsar', 'DM1_err')

        # Deleting field 'Pulsar.RM'
        db.delete_column(u'database_pulsar', 'RM')

        # Deleting field 'Pulsar.RM_err'
        db.delete_column(u'database_pulsar', 'RM_err')

        # Deleting field 'Pulsar.W50'
        db.delete_column(u'database_pulsar', 'W50')

        # Deleting field 'Pulsar.W50_err'
        db.delete_column(u'database_pulsar', 'W50_err')

        # Deleting field 'Pulsar.W10'
        db.delete_column(u'database_pulsar', 'W10')

        # Deleting field 'Pulsar.W10_err'
        db.delete_column(u'database_pulsar', 'W10_err')

        # Deleting field 'Pulsar.Tau_sc'
        db.delete_column(u'database_pulsar', 'Tau_sc')

        # Deleting field 'Pulsar.Tau_sc_err'
        db.delete_column(u'database_pulsar', 'Tau_sc_err')

        # Deleting field 'Pulsar.S400'
        db.delete_column(u'database_pulsar', 'S400')

        # Deleting field 'Pulsar.S400_err'
        db.delete_column(u'database_pulsar', 'S400_err')

        # Deleting field 'Pulsar.S1400'
        db.delete_column(u'database_pulsar', 'S1400')

        # Deleting field 'Pulsar.S1400_err'
        db.delete_column(u'database_pulsar', 'S1400_err')

        # Deleting field 'Pulsar.S2000'
        db.delete_column(u'database_pulsar', 'S2000')

        # Deleting field 'Pulsar.S2000_err'
        db.delete_column(u'database_pulsar', 'S2000_err')

        # Deleting field 'Pulsar.spindx'
        db.delete_column(u'database_pulsar', 'spindx')

        # Deleting field 'Pulsar.spindx_err'
        db.delete_column(u'database_pulsar', 'spindx_err')

        # Deleting field 'Pulsar.Binary'
        db.delete_column(u'database_pulsar', 'Binary')

        # Deleting field 'Pulsar.T0'
        db.delete_column(u'database_pulsar', 'T0')

        # Deleting field 'Pulsar.T0_err'
        db.delete_column(u'database_pulsar', 'T0_err')

        # Deleting field 'Pulsar.PB'
        db.delete_column(u'database_pulsar', 'PB')

        # Deleting field 'Pulsar.PB_err'
        db.delete_column(u'database_pulsar', 'PB_err')

        # Deleting field 'Pulsar.A1'
        db.delete_column(u'database_pulsar', 'A1')

        # Deleting field 'Pulsar.A1_err'
        db.delete_column(u'database_pulsar', 'A1_err')

        # Deleting field 'Pulsar.OM'
        db.delete_column(u'database_pulsar', 'OM')

        # Deleting field 'Pulsar.OM_err'
        db.delete_column(u'database_pulsar', 'OM_err')

        # Deleting field 'Pulsar.ECC'
        db.delete_column(u'database_pulsar', 'ECC')

        # Deleting field 'Pulsar.Ecc_err'
        db.delete_column(u'database_pulsar', 'Ecc_err')

        # Deleting field 'Pulsar.TASC'
        db.delete_column(u'database_pulsar', 'TASC')

        # Deleting field 'Pulsar.TASC_err'
        db.delete_column(u'database_pulsar', 'TASC_err')

        # Deleting field 'Pulsar.Eps1'
        db.delete_column(u'database_pulsar', 'Eps1')

        # Deleting field 'Pulsar.Eps1_err'
        db.delete_column(u'database_pulsar', 'Eps1_err')

        # Deleting field 'Pulsar.Eps2'
        db.delete_column(u'database_pulsar', 'Eps2')

        # Deleting field 'Pulsar.Eps2_err'
        db.delete_column(u'database_pulsar', 'Eps2_err')

        # Deleting field 'Pulsar.MinMass'
        db.delete_column(u'database_pulsar', 'MinMass')

        # Deleting field 'Pulsar.MedMass'
        db.delete_column(u'database_pulsar', 'MedMass')

        # Deleting field 'Pulsar.BinComp'
        db.delete_column(u'database_pulsar', 'BinComp')

        # Deleting field 'Pulsar.Dist'
        db.delete_column(u'database_pulsar', 'Dist')

        # Deleting field 'Pulsar.Dist_DM'
        db.delete_column(u'database_pulsar', 'Dist_DM')

        # Deleting field 'Pulsar.DMsinb'
        db.delete_column(u'database_pulsar', 'DMsinb')

        # Deleting field 'Pulsar.ZZ'
        db.delete_column(u'database_pulsar', 'ZZ')

        # Deleting field 'Pulsar.XX'
        db.delete_column(u'database_pulsar', 'XX')

        # Deleting field 'Pulsar.YY'
        db.delete_column(u'database_pulsar', 'YY')

        # Deleting field 'Pulsar.Assoc'
        db.delete_column(u'database_pulsar', 'Assoc')

        # Deleting field 'Pulsar.Survey'
        db.delete_column(u'database_pulsar', 'Survey')

        # Deleting field 'Pulsar.OSurvey'
        db.delete_column(u'database_pulsar', 'OSurvey')

        # Deleting field 'Pulsar.Date'
        db.delete_column(u'database_pulsar', 'Date')

        # Deleting field 'Pulsar.Type'
        db.delete_column(u'database_pulsar', 'Type')

        # Deleting field 'Pulsar.NGlt'
        db.delete_column(u'database_pulsar', 'NGlt')

        # Deleting field 'Pulsar.R_Lum'
        db.delete_column(u'database_pulsar', 'R_Lum')

        # Deleting field 'Pulsar.R_Lum14'
        db.delete_column(u'database_pulsar', 'R_Lum14')

        # Deleting field 'Pulsar.Age'
        db.delete_column(u'database_pulsar', 'Age')

        # Deleting field 'Pulsar.BSurf'
        db.delete_column(u'database_pulsar', 'BSurf')

        # Deleting field 'Pulsar.Edot'
        db.delete_column(u'database_pulsar', 'Edot')

        # Deleting field 'Pulsar.Edotd2'
        db.delete_column(u'database_pulsar', 'Edotd2')

        # Deleting field 'Pulsar.PMTot'
        db.delete_column(u'database_pulsar', 'PMTot')

        # Deleting field 'Pulsar.VTrans'
        db.delete_column(u'database_pulsar', 'VTrans')

        # Deleting field 'Pulsar.P1_i'
        db.delete_column(u'database_pulsar', 'P1_i')

        # Deleting field 'Pulsar.Age_i'
        db.delete_column(u'database_pulsar', 'Age_i')

        # Deleting field 'Pulsar.BSurf_i'
        db.delete_column(u'database_pulsar', 'BSurf_i')

        # Deleting field 'Pulsar.Edot_i'
        db.delete_column(u'database_pulsar', 'Edot_i')

        # Deleting field 'Pulsar.B_LC'
        db.delete_column(u'database_pulsar', 'B_LC')


    models = {
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
            'Binary': ('django.db.models.fields.CharField', [], {'default': "'*'", 'max_length': '200'}),
            'DM': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'DM1': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'DM1_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'DM_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'DMsinb': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Date': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'DecJ': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
            'DecJD': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'DecJ_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Dist': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Dist_DM': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ECC': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ELat': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ELat_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ELong': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ELong_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'Ecc_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
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
            'RAJD': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'RM': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'RM_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'R_Lum': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'R_Lum14': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'RaJ': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '200'}),
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
            'VTrans': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'W10': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'W10_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'W50': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'W50_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'XX': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'YY': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'ZZ': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spindx': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'spindx_err': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        }
    }

    complete_apps = ['database']