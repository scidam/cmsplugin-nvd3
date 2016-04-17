# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NVD3Model'
        db.create_table(u'cmsplugin_nvd3model', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('chart_type', self.gf('django.db.models.fields.CharField')(default='lineChart', max_length=30)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=600, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=400, blank=True)),
            ('color_category', self.gf('django.db.models.fields.CharField')(default='category10', max_length=15, blank=True)),
            ('x_is_date', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('x_date_format', self.gf('django.db.models.fields.CharField')(default='%d %b %Y', max_length=15, blank=True)),
            ('xdata', self.gf('django.db.models.fields.TextField')()),
            ('ydata', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('ynames', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('container_name', self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True)),
            ('attrs', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'cmsplugin_nvd3', ['NVD3Model'])


    def backwards(self, orm):
        # Deleting model 'NVD3Model'
        db.delete_table(u'cmsplugin_nvd3model')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_nvd3.nvd3model': {
            'Meta': {'object_name': 'NVD3Model', 'db_table': "u'cmsplugin_nvd3model'"},
            'attrs': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'chart_type': ('django.db.models.fields.CharField', [], {'default': "'lineChart'", 'max_length': '30'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color_category': ('django.db.models.fields.CharField', [], {'default': "'category10'", 'max_length': '15', 'blank': 'True'}),
            'container_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '400', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '600', 'blank': 'True'}),
            'x_date_format': ('django.db.models.fields.CharField', [], {'default': "'%d %b %Y'", 'max_length': '15', 'blank': 'True'}),
            'x_is_date': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'xdata': ('django.db.models.fields.TextField', [], {}),
            'ydata': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'ynames': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_nvd3']