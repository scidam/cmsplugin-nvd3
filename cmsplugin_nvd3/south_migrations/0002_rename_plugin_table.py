# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models, connection
import cms

class Migration(SchemaMigration):

    def forwards(self, orm):
        table_names = connection.introspection.table_names()
        if 'cmsplugin_nvd3model' in table_names and\
            cms.__version__.startswith('3.0'):
            db.rename_table('cmsplugin_nvd3model', 'cmsplugin_nvd3_nvd3model')

    def backwards(self, orm):
        table_names = connection.introspection.table_names()
        if 'cmsplugin_nvd3_nvd3model' in table_names:
            db.rename_table('cmsplugin_nvd3_nvd3model', 'cmsplugin_nvd3model')
