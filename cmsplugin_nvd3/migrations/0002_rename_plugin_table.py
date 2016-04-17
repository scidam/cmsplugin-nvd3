# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, connection
import cms


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_nvd3', '0001_initial'),
    ]

    _table_names = connection.introspection.table_names()
    if 'cmsplugin_nvd3model' in _table_names and\
        cms.__version__.startswith('3.'):
        operations = [migrations.AlterModelTable('cmsplugin_nvd3model',
                                              'cmsplugin_nvd3_nvd3model')]
    else:
        operations = []
