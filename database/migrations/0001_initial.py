# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'XrayComponent'
        db.create_table(u'database_xraycomponent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('psr_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['database.Pulsar'], null=True, blank=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('spec_type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lum', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('lum_plus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('lum_minus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('flux', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('flux_plus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('flux_minus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('t', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('t_plus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('t_minus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('r', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('r_plus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('r_minus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pl', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pl_plus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pl_minus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('b_atm', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'database', ['XrayComponent'])

        # Adding model 'XrayFit'
        db.create_table(u'database_xrayfit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('psr_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['database.Pulsar'], null=True, blank=True)),
            ('ordinal', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('spectrum', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'database', ['XrayFit'])

        # Adding M2M table for field components on 'XrayFit'
        db.create_table(u'database_xrayfit_components', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('xrayfit', models.ForeignKey(orm[u'database.xrayfit'], null=False)),
            ('xraycomponent', models.ForeignKey(orm[u'database.xraycomponent'], null=False))
        ))
        db.create_unique(u'database_xrayfit_components', ['xrayfit_id', 'xraycomponent_id'])

        # Adding model 'XrayArticle'
        db.create_table(u'database_xrayarticle', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('article', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('cite', self.gf('django.db.models.fields.TextField')(default='\\cite{}')),
            ('info', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('dist', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'database', ['XrayArticle'])

        # Adding M2M table for field fits on 'XrayArticle'
        db.create_table(u'database_xrayarticle_fits', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('xrayarticle', models.ForeignKey(orm[u'database.xrayarticle'], null=False)),
            ('xrayfit', models.ForeignKey(orm[u'database.xrayfit'], null=False))
        ))
        db.create_unique(u'database_xrayarticle_fits', ['xrayarticle_id', 'xrayfit_id'])

        # Adding model 'Geometry'
        db.create_table(u'database_geometry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('article', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('cite', self.gf('django.db.models.fields.TextField')(default='\\cite{}')),
            ('info', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('alpha', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('beta', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('rho', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'database', ['Geometry'])

        # Adding model 'Subpulse'
        db.create_table(u'database_subpulse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('article', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('cite', self.gf('django.db.models.fields.TextField')(default='\\cite{}')),
            ('info', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('p2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('p2_plus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('p2_minus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('p3', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('p3_plus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('p3_minus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('p4', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'database', ['Subpulse'])

        # Adding model 'Additional'
        db.create_table(u'database_additional', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('articles', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('best_age', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dist_dm_cl', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dist_dm_cl_plus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dist_dm_cl_minus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dist_pi', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dist_pi_plus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dist_pi_minus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'database', ['Additional'])

        # Adding model 'Calculation'
        db.create_table(u'database_calculation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cos_i', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('f', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dotP_15', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('bsurf2', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('b_14dp', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('l_sd', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('a_dp', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('r_dp', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('a', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('b', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('b_14', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('b_14_plus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('b_14_minus', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'database', ['Calculation'])

        # Adding model 'Pulsar'
        db.create_table(u'database_pulsar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('jname', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('raj', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('raj_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('decj', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('decj_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('pmra', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('pmra_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('pmdec', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('pmdec_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('px', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('px_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('posepoch', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('elong', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('elong_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('elat', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('elat_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('pmelong', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('pmelong_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('pmelat', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('pmelat_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('gl', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('gb', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('rajd', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('decjd', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('p0', self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=22, decimal_places=20)),
            ('p0_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('p1', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('p1_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('f0', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('f0_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('f1', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('f1_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('f2', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('f2_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('f3', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('f3_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('pepoch', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('dm', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('dm_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('dm1', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('dm1_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('rm', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('rm_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('w50', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('w50_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('w10', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('w10_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('units', self.gf('django.db.models.fields.CharField')(default=None, max_length=200)),
            ('tau_sc', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('tau_sc_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('s400', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('s400_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('s1400', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('s1400_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('s2000', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('s2000_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('spindx', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('spindx_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('binary', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('t0', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('t0_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('pb', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('pb_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('a1', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('a1_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('om', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('om_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('ecc', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('ecc_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('tasc', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('tasc_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('eps1', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('eps1_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('eps2', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('eps2_err', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('minmass', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('medmass', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('bincomp', self.gf('django.db.models.fields.CharField')(default=None, max_length=200)),
            ('dist', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('dist_dm', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('dmsinb', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('zz', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('xx', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('yy', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('assoc', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('survey', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('osurvey', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default=None, max_length=200, null=True, blank=True)),
            ('nglt', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('r_lum', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('r_lum14', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('age', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('bsurf', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('edot', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('edotd2', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('pmtot', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('vtrans', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('p1_i', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('age_i', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('bsurf_i', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('edot_i', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('b_lc', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
            ('simbad_link', self.gf('django.db.models.fields.TextField')(default='http://simbad.u-strasbg.fr')),
            ('comment', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
            ('lum_malov', self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal(u'database', ['Pulsar'])

        # Adding M2M table for field xray_articles on 'Pulsar'
        db.create_table(u'database_pulsar_xray_articles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pulsar', models.ForeignKey(orm[u'database.pulsar'], null=False)),
            ('xrayarticle', models.ForeignKey(orm[u'database.xrayarticle'], null=False))
        ))
        db.create_unique(u'database_pulsar_xray_articles', ['pulsar_id', 'xrayarticle_id'])

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
        # Deleting model 'XrayComponent'
        db.delete_table(u'database_xraycomponent')

        # Deleting model 'XrayFit'
        db.delete_table(u'database_xrayfit')

        # Removing M2M table for field components on 'XrayFit'
        db.delete_table('database_xrayfit_components')

        # Deleting model 'XrayArticle'
        db.delete_table(u'database_xrayarticle')

        # Removing M2M table for field fits on 'XrayArticle'
        db.delete_table('database_xrayarticle_fits')

        # Deleting model 'Geometry'
        db.delete_table(u'database_geometry')

        # Deleting model 'Subpulse'
        db.delete_table(u'database_subpulse')

        # Deleting model 'Additional'
        db.delete_table(u'database_additional')

        # Deleting model 'Calculation'
        db.delete_table(u'database_calculation')

        # Deleting model 'Pulsar'
        db.delete_table(u'database_pulsar')

        # Removing M2M table for field xray_articles on 'Pulsar'
        db.delete_table('database_pulsar_xray_articles')

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
            'articles': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
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
            'article': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'beta': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cite': ('django.db.models.fields.TextField', [], {'default': "'\\\\cite{}'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rho': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'database.pulsar': {
            'Meta': {'object_name': 'Pulsar'},
            'a1': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'a1_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'additionals': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.Additional']", 'symmetrical': 'False'}),
            'age': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'age_i': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'assoc': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'b_lc': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'binary': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'bincomp': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200'}),
            'bsurf': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'bsurf_i': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'calculations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.Calculation']", 'symmetrical': 'False'}),
            'comment': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'decj': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'decj_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'decjd': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'dist': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'dist_dm': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'dm': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'dm1': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'dm1_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'dm_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'dmsinb': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'ecc': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'ecc_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'edot': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'edot_i': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'edotd2': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'elat': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'elat_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'elong': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'elong_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'eps1': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'eps1_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'eps2': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'eps2_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'f0': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'f0_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'f1': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'f1_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'f2': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'f2_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'f3': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'f3_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'gb': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'geometries': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.Geometry']", 'symmetrical': 'False'}),
            'gl': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jname': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'lum_malov': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'medmass': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'minmass': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nglt': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'om': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'om_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'osurvey': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'p0': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'max_digits': '22', 'decimal_places': '20'}),
            'p0_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'p1': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'p1_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'p1_i': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pb': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pb_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pepoch': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pmdec': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pmdec_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pmelat': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pmelat_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pmelong': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pmelong_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pmra': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pmra_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'pmtot': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'posepoch': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'px': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'px_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'r_lum': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'r_lum14': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'raj': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'raj_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rajd': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rm': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rm_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            's1400': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            's1400_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            's2000': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            's2000_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            's400': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            's400_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'simbad_link': ('django.db.models.fields.TextField', [], {'default': "'http://simbad.u-strasbg.fr'"}),
            'spindx': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'spindx_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'subpulses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.Subpulse']", 'symmetrical': 'False'}),
            'survey': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            't0': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            't0_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'tasc': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'tasc_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'tau_sc': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'tau_sc_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'units': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200'}),
            'vtrans': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'w10': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'w10_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'w50': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'w50_err': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'xray_articles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.XrayArticle']", 'symmetrical': 'False'}),
            'xx': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'yy': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'zz': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'database.subpulse': {
            'Meta': {'object_name': 'Subpulse'},
            'article': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'cite': ('django.db.models.fields.TextField', [], {'default': "'\\\\cite{}'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
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
            'article': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'cite': ('django.db.models.fields.TextField', [], {'default': "'\\\\cite{}'"}),
            'dist': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fits': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['database.XrayFit']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
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
            'psr_id': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['database.Pulsar']", 'null': 'True', 'blank': 'True'}),
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
            'psr_id': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['database.Pulsar']", 'null': 'True', 'blank': 'True'}),
            'spectrum': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['database']